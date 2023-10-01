from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from config import WEB_APP_HOST
from routes.events import router as event_router
from routes.schedules import router as schedule_router
from routes.user import router as user_router
from scheduler.scheduler import scheduler

app = FastAPI()

scheduler.start()

origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    WEB_APP_HOST
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS", "DELETE", "PATCH", "PUT"],
    allow_headers=["*"],
)

app.include_router(
    user_router,
    prefix="/user",
    tags=["user"]
)
app.include_router(
    event_router,
    prefix="/event",
    tags=["event"]
)
app.include_router(
    schedule_router,
    prefix="/schedule",
    tags=["schedule"]
)
