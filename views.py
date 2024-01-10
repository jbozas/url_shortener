from fastapi import APIRouter, Depends, HTTPException, Request
from sqlmodel import Session
from pydantic import BaseModel
from fastapi.responses import RedirectResponse

from database import get_session
from utils.logger import logger_config
from url_shorted.crud import create_url_shorted, search_url_shorted
from url_shorted.models import UrlShorted

router = APIRouter()

logger = logger_config(__name__)


class ShorterParams(BaseModel):
    url: str


@router.post("/shorten/")
async def shorten_url(
    url_input: ShorterParams,
    db: Session = Depends(get_session),
    request: Request = None,
):
    url: UrlShorted = await create_url_shorted(
        UrlShorted(url_original=url_input.url), db
    )

    return {"shortened_url": f"{request.base_url}r/{url.url_shorted}"}


@router.get("/r/{url_shorted}")
async def redirect_to_original(url_shorted: str, db: Session = Depends(get_session)):
    url: UrlShorted = await search_url_shorted(url_shorted, db)
    if url is None:
        raise HTTPException(status_code=404, detail="URL not found")
    return RedirectResponse(url.url_original)
