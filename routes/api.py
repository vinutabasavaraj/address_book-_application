from fastapi import APIRouter
from src.endpoints import (create_table)

router = APIRouter()

router.include_router(create_table.router)