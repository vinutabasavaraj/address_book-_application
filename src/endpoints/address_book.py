from fastapi import APIRouter,Depends, HTTPException,status,Query
from sqlalchemy.orm import Session

from src.common.connect_db import get_db
from src.models.sqlite_orm_model import AddressModel

from src.address_book_operations.create_address_book import create_address_book
from src.address_book_operations.update_address_book import update_address_book
from src.address_book_operations.delete_address_book import delete_address_book
from src.address_book_operations.get_address_book_details import get_address_book_details
from src.schemas.address_model import address


router = APIRouter(
    tags=["Manage Book"]
)

@router.post("/address",status_code=201)
async def create_address(info:address,db: Session = Depends(get_db)):
    '''API to create an Address'''
    try:
        response = await create_address_book(info, db)
        return {"detail": {"message": "Address added successfully", "data": response, "statusCode": 201}}
    
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail={"message": {str(e)}, "statusCode": 500})
    
@router.put("/address/{address_id}")
async def update_address(address_id: int,info:address,db: Session = Depends(get_db)):
    '''API to update an Address'''
    address_details = db.query(AddressModel).filter(AddressModel.id == address_id).first()
    if address_details is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={"message":"Id not found", "statusCode": 404})

    else:
        try:
            response = await update_address_book(info,address_id, db)
            return {"detail": {"message": "Address updated successfully", "data": response, "statusCode": 200}}
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail={"message": {str(e)}, "statusCode": 500})
        
@router.delete("/address/{address_id}")
async def update_address(address_id: int,db: Session = Depends(get_db)):
    '''API to remove an Address'''
    address_details = db.query(AddressModel).filter(AddressModel.id == address_id).first()
    if address_details is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={"message":"Id not found", "statusCode": 404})
    else:
        try:
            response = await delete_address_book(address_id, db)
            return {"detail": {"message": "Address deleted successfully", "data": response, "statusCode": 200}}
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail={"message": {str(e)}, "statusCode": 500})


@router.get("/address")
async def get_addresses_within_distance(latitude: float = Query(..., description="Latitude of the location"),
                                  longitude: float = Query(..., description="Longitude of the location"),
                                  distance: float = Query(..., description="Maximum distance in kilometers"),db: Session = Depends(get_db)):
    address_details = db.query(AddressModel).all()
    if address_details == []:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={"message":"Id not found", "statusCode": 404})
    else:
        try:
            response = await get_address_book_details(address_details,latitude,longitude,distance)
            return {"detail": {"message": "Address deleted successfully", "data": response, "statusCode": 200}}
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail={"message": {str(e)}, "statusCode": 500})



    


    
   



