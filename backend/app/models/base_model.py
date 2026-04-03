from datetime import datetime
from typing import Any, Optional

from pydantic import BaseModel, ConfigDict, Field

try:
    from bson import ObjectId
except ModuleNotFoundError:
    class ObjectId(str):
        @staticmethod
        def is_valid(value: Any) -> bool:
            return isinstance(value, str) and len(value) == 24

        def __new__(cls, value: str) -> "ObjectId":
            return str.__new__(cls, value)


class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, value: Any) -> ObjectId:
        if isinstance(value, ObjectId):
            return value
        if isinstance(value, str) and ObjectId.is_valid(value):
            return ObjectId(value)
        raise ValueError("Invalid ObjectId")

    @classmethod
    def __get_pydantic_json_schema__(cls, core_schema: Any, handler: Any) -> dict[str, Any]:
        return {"type": "string"}


class MongoModel(BaseModel):
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
        json_encoders={ObjectId: str},
    )


class TimestampMixin(MongoModel):
    id: Optional[PyObjectId] = Field(default=None, alias="_id")
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: Optional[datetime] = Field(default_factory=datetime.utcnow)
