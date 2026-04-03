from datetime import datetime
from typing import Optional

from pydantic import Field

from app.models.base_model import PyObjectId, TimestampMixin


class FacultyAssignment(TimestampMixin):
    complaint_id: PyObjectId = Field(..., description="Foreign key reference to complaints._id")
    faculty_id: PyObjectId = Field(..., description="Foreign key reference to users._id")
    department_id: PyObjectId = Field(..., description="Foreign key reference to departments._id")
    assigned_at: datetime = Field(default_factory=datetime.utcnow)
    assigned_by: Optional[PyObjectId] = Field(
        default=None,
        description="Optional foreign key reference to users._id",
    )
