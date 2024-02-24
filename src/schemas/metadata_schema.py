from typing import Optional
from typing import List
from pydantic import AnyUrl, BaseModel, Field


class metadata_sqlite(BaseModel):
    '''
    This class represents metadata for a SQLite database, specifying the path to the database file
    '''
    databaseName : str = Field(example="databaseName",min_length=1)