from fastapi import Depends
from sqlmodel import Session, select

from url_shorted.models import UrlShorted
from services import Tokenize
from database import get_session


async def create_url_shorted(
    url_shorted: UrlShorted, db: Session = Depends(get_session)
):
    url_token = await Tokenize.generate_shorter_link()
    url_shorted.url_shorted = url_token
    url_shorted = UrlShorted.model_validate(url_shorted)
    db.add(url_shorted)
    db.commit()
    db.refresh(url_shorted)
    return url_shorted


async def search_url_shorted(url_shorted: str, db: Session = Depends(get_session)):
    return db.exec(
        select(UrlShorted).where(UrlShorted.url_shorted == url_shorted)
    ).first()
