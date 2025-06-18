from fastapi import APIRouter

import logging

router = APIRouter()

@router.get("/", include_in_schema=False)
def root_response():
    return {"status":True,"message":"Root api is working","data":{}}