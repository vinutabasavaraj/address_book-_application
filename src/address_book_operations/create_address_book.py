
from fastapi import HTTPException,status
from src.models.sqlite_orm_model import AddressModel



# API to create a new address
async def create_address_book(info, db):
    try:
    # Validate address data
        if not (-90 <= info.latitude <= 90):
            raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="Latitude out of range")
        if not (-180 <= info.longitude <= 180):
            raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="Longitude out of range")
        address_info = AddressModel(name = info.name, street = info.street, city = info.city, state = info.state, zip_code = info.zip_code, latitude =  info.latitude, longitude = info.longitude)
        db.add(address_info)
        db.commit()
        db.refresh(address_info)
        return info
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail={"message": {str(e)}, "statusCode": 500}
        )

        

