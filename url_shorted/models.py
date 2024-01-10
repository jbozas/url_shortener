from typing import Optional

from sqlmodel import Field, SQLModel


class UrlShorted(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    url_shorted: str = Field(index=True)
    url_original: str = Field(...)
