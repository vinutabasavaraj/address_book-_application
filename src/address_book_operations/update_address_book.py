from fastapi import HTTPException,status
from src.models.sqlite_orm_model import AddressModel

# Method to update the specified address
async def update_address_book(info,address_id, db):
    try:
        db.query(AddressModel).filter(AddressModel.id == address_id).\
                update({AddressModel.name : info.name,
                        AddressModel.street: info.street,
                        AddressModel.city: info.city,
                        AddressModel.state: info.state,
                        AddressModel.zip_code: info.zip_code,
                        AddressModel.latitude: info.latitude,
                        AddressModel.longitude: info.longitude
                        })
        db.commit()
        return info
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail={"message": {str(e)}, "statusCode": 500}
        )


       
    