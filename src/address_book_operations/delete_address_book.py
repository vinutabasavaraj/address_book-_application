from fastapi import HTTPException,status
from src.models.sqlite_orm_model import AddressModel


# Method to remove the specified address
async def delete_address_book(address_id, db):
    try:
        address_details = db.query(AddressModel).filter(AddressModel.id == address_id).first()
        db.delete(address_details)
        db.commit()
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail={"message": {str(e)}, "statusCode": 500})