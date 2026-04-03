from datetime import datetime
from enum import Enum

from pydantic import Field

from app.models.base_model import PyObjectId, TimestampMixin


class AttachmentType(str, Enum):
    IMAGE = "image"
    VIDEO = "video"
    DOCUMENT = "document"


class Attachment(TimestampMixin):
    complaint_id: PyObjectId = Field(..., description="Foreign key reference to complaints._id")
    uploaded_by: PyObjectId = Field(..., description="Foreign key reference to users._id")
    file_url: str
    file_type: AttachmentType
    file_name: str
    uploaded_at: datetime = Field(default_factory=datetime.utcnow)
