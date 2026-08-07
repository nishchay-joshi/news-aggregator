from datetime import time

from pydantic import BaseModel


class UpdatePreferencesRequest(BaseModel):
    interests: list[str]
    custom_sources: list[str]


class UpdateEmailTimeRequest(BaseModel):
    email_delivery_time: time