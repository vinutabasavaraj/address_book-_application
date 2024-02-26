
from fastapi import HTTPException,status
from src.models.sqlite_orm_model import AddressModel



# Method to create a new address
async def create_address_book(info, db):
    try:
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

        

