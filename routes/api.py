from fastapi import APIRouter
from src.endpoints import (create_table, address_book)

router = APIRouter()

router.include_router(create_table.router)
router.include_router(address_book.router)