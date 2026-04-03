from datetime import datetime
from enum import Enum

from pydantic import Field

from app.models.base_model import PyObjectId, TimestampMixin


class NotificationType(str, Enum):
    ESCALATION = "ESCALATION"
    RESOLUTION = "RESOLUTION"
    ASSIGNMENT = "ASSIGNMENT"


class Notification(TimestampMixin):
    user_id: PyObjectId = Field(..., description="Foreign key reference to users._id")
    complaint_id: PyObjectId = Field(..., description="Foreign key reference to complaints._id")
    type: NotificationType
    message: str
    is_read: bool = False
    email_sent: bool = False
    sent_at: datetime = Field(default_factory=datetime.utcnow)
