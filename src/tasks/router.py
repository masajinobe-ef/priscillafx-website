# FastAPI
from fastapi import APIRouter, Depends

# Auth depends
from auth.config import current_user

# Tasks events
from .tasks import send_email_report_hello


router = APIRouter(prefix="/report", tags=["Tasks"])


@router.get("/email")
def send_email_report(user=Depends(current_user)):
    send_email_report_hello.delay(user.username)
    return {
        "status": "Success",
        "data": None,
        "details": "Email has been sent",
    }
