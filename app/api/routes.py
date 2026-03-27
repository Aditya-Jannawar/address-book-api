from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.models.address import Address
from app.schemas.address import AddressCreate, AddressUpdate, AddressResponse
from geopy.distance import geodesic
from app.utils.logger import logger


API_V1_PREFIX = "/api/v1" # API Versioning
router = APIRouter(prefix=f"{API_V1_PREFIX}/addresses")


# CREATE
@router.post("/", response_model=AddressResponse)
def create_address(address: AddressCreate, db: Session = Depends(get_db)):
    logger.info("Creating new address")

    try:
        new_address = Address(**address.dict())
        db.add(new_address)
        db.commit()
        db.refresh(new_address)
        return new_address

    except Exception as e:
        logger.error(f"Error creating address: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal Server Error")


# GET ALL
@router.get("/", response_model=list[AddressResponse])
def get_addresses(db: Session = Depends(get_db)) -> list[Address]:
    logger.info("Fetching all addresses")

    try:
        return db.query(Address).all()

    except Exception as e:
        logger.error(f"Error fetching addresses: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal Server Error")


# 🌍 Nearby Addresses (IMPORTANT: placed before /{id})
@router.get("/nearby", response_model=list[AddressResponse])
def get_nearby_addresses(
    latitude: float = Query(..., ge=-90, le=90),
    longitude: float = Query(..., ge=-180, le=180),
    distance: float = Query(..., gt=0),  # must be > 0
    db: Session = Depends(get_db)
):
    logger.info(f"Fetching nearby addresses within {distance} km")

    try:
        addresses = db.query(Address).all()
        nearby_addresses = []

        for addr in addresses:
            dist = geodesic(
                (latitude, longitude),
                (addr.latitude, addr.longitude)
            ).km

            if dist <= distance:
                nearby_addresses.append(addr)

        return nearby_addresses

    except Exception as e:
        logger.error(f"Error fetching nearby addresses: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal Server Error")


# GET ONE
@router.get("/{address_id}", response_model=AddressResponse)
def get_address(address_id: int, db: Session = Depends(get_db)):
    logger.info(f"Fetching address with id {address_id}")

    try:
        address = db.query(Address).filter(Address.id == address_id).first()

        if not address:
            logger.warning(f"Address not found with id {address_id}")
            raise HTTPException(status_code=404, detail="Address not found")

        return address

    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error fetching address: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal Server Error")


# UPDATE
@router.put("/{address_id}", response_model=AddressResponse)
def update_address(address_id: int, updated_data: AddressUpdate, db: Session = Depends(get_db)):
    logger.info(f"Updating address with id {address_id}")

    try:
        address = db.query(Address).filter(Address.id == address_id).first()

        if not address:
            logger.warning(f"Address not found for update with id {address_id}")
            raise HTTPException(status_code=404, detail="Address not found")

        for key, value in updated_data.dict(exclude_unset=True).items():
            setattr(address, key, value)

        db.commit()
        db.refresh(address)

        return address

    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error updating address: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal Server Error")


# DELETE
@router.delete("/{address_id}")
def delete_address(address_id: int, db: Session = Depends(get_db)):
    logger.info(f"Deleting address with id {address_id}")

    try:
        address = db.query(Address).filter(Address.id == address_id).first()

        if not address:
            logger.warning(f"Address not found for deletion with id {address_id}")
            raise HTTPException(status_code=404, detail="Address not found")

        db.delete(address)
        db.commit()

        return {"message": "Address deleted successfully"}

    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error deleting address: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal Server Error")