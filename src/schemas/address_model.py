from pydantic import BaseModel, Field


class address(BaseModel):
    '''
    Model to represent an address with coordinates.
    '''
    name : str = Field(description="Name of the place or location",min_length=1)
    street : str = Field(description="Street address",min_length=1)
    city : str = Field(description="City",min_length=1)
    state : str = Field(description="State or region",min_length=1)
    zip_code : str = Field(description="ZIP or postal code",min_length=1)
    latitude: float = Field(ge=-90, le=90, description="Latitude value in the range -90 to 90")
    longitude: float = Field(ge=-180, le=180, description="Longitude value in the range -180 to 180")