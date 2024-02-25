from fastapi import APIRouter
from sqlalchemy import create_engine
from fastapi import HTTPException,status
from pathlib import Path
import json

from src.schemas.metadata_schema import metadata_sqlite
from src.models.sqlite_orm_model import Base
from .check_path_db import check_path_permission
from src.log_management.generate_info_logs import generate_info_logs
from src.log_management.generate_error_logs import generate_error_logs

router=APIRouter(tags=["CreateTable"])

current_directory_path = Path(__file__).parents[2]
properties_filename = current_directory_path/'properties.json'

#Method to store the database details in json file
async def metadata_configuration(new_data):
    with open(properties_filename,'r+',encoding='utf-8') as file:
        file_data = json.load(file)
        file_data["metadata_config"]=new_data
        file.seek(0)
        file.truncate()
        json.dump(file_data, file,ensure_ascii = False, indent = 4)

#API to create the table
@router.post('/create_table')
async def create_tables(db_details:metadata_sqlite):
    """API to Create the Tables:\n
    Request Body:\n
    - DatabaseName : Path to the database file.\n
    """

    info_log = generate_info_logs('address_info')
    error_log = generate_error_logs('address_error')

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
            info_log.info("Tables created successfully.")
            return {"detail": {"message": "Tables created successfully.", "statusCode": 201, "errorCode": None}} 
        except Exception as e:
            error_log.exception(e,exc_info=True)
            raise HTTPException(
                status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
                detail={"message": f"Creation of tables failed: {str(e)}", "statusCode": 503, "errorCode": "errorcode"}
            )
    else:
        error_log.error(str(message))
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={"message":message, "statusCode": 404})
        



