import os
import logging

from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI

from src.routers import (
    root_api,
    podcast_api
)


app = FastAPI(title="PDF to Podcast")

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)


app.include_router(root_api, prefix="", tags=["Root Page"])
app.include_router(podcast_api, prefix="", tags=["Podcast API"])