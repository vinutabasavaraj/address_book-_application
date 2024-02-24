from pydantic import BaseModel, Field


class address(BaseModel):
    '''
    Model to accept the database path
    '''
    name : str 
    street : str 
    city : str 
    state : str 
    zip_code : str 
    latitude : float 
    longitude : float 
