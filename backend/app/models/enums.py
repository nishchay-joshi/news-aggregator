from enum import Enum


class ContentType(str, Enum):
    NEWS = "news"
    BLOG = "blog"
    YOUTUBE = "youtube"


class EmailStatus(str, Enum):
    SUCCESS = "success"
    FAILED = "failed"