from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from DataBase.db import base, engine
from error import exception, exceptionHandle
from route import route


# Create database tables
base.metadata.create_all(bind=engine)

# Initialize FastAPI application
app = FastAPI(title="Task Manager")

# Register API routes
app.include_router(route.route)

# Register custom exception handler
app.add_exception_handler(
    exception.DatabaseException,
    exceptionHandle.db_handler,
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)
