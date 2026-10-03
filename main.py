from fastapi import FastAPI  # type: ignore[import-not-found]
from DataBase.db import base,engine
from error import exception,exceptionHandle
from route import route
from fastapi.middleware.cors import CORSMiddleware
base.metadata.create_all(engine)
app=FastAPI(title="task Manager")


base.metadata.create_all(engine)
app.include_router(route.route)
app.add_exception_handler(exception.DatabaseException, exceptionHandle.db_handler)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)