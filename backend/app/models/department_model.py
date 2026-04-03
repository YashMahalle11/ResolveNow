from enum import Enum

from pydantic import Field

from app.models.base_model import PyObjectId, TimestampMixin


class DepartmentName(str, Enum):
    BEHAVIOURAL = "BEHAVIOURAL"
    INFRASTRUCTURAL = "INFRASTRUCTURAL"
    ACADEMIC = "ACADEMIC"
    GENERAL = "GENERAL"


class DepartmentPriority(str, Enum):
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"


class Department(TimestampMixin):
    name: DepartmentName
    description: str
    default_priority: DepartmentPriority = DepartmentPriority.MEDIUM
    faculty_user_ids: list[PyObjectId] = Field(
        default_factory=list,
        description="Embedded list of user ids belonging to this department",
    )
