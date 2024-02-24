from fastapi import APIRouter
from sqlalchemy import create_engine
from fastapi import HTTPException,status
from pathlib import Path
import json

from src.schemas.metadata_schema import metadata_sqlite
from src.models.sqlite_orm_model import Base
from .check_path_db import check_path_permission

router=APIRouter(tags=["CreateTable"])

cwd = Path(__file__).parents[1]
filepath = cwd/'common'/'metadata_info.json'

#Method to store the database details in json file
async def metadata_configuration(new_data):
    with open(filepath,'r+',encoding='utf-8') as file:
        file_data = json.load(file)
        file_data["metadata_config"]=new_data
        file.seek(0)
        file.truncate()
        json.dump(file_data, file,ensure_ascii = False, indent = 4)

#API to create the table
@router.post('/create_table')
async def create_tables(db_details:metadata_sqlite):
    """API to Create the Tables:
    Request Body:
    - DatabaseName : Path to the database file.
    """
    status_value, message = check_path_permission(db_details.databaseName)
    if status_value:
        try:     

            SQLALCHEMY_DATABASE_URL = "sqlite:///" +  db_details.databaseName
            engine = create_engine(SQLALCHEMY_DATABASE_URL,pool_size=20, max_overflow=0)
            engine.connect()
            
            Base.metadata.create_all(engine)
            
            metadata_config = {
                                "databaseType": "sqlite",
                                "databaseName": db_details.databaseName
                            }
                        
            await metadata_configuration(metadata_config)
            return {"detail": {"message": "Tables created successfully.", "statusCode": 201, "errorCode": None}} 
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
                detail={"message": f"Creation of tables failed: {str(e)}", "statusCode": 503, "errorCode": "errorcode"}
            )
    else:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail={"message":message, "statusCode": 403})
        



