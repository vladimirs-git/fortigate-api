"""schema/models."""

from typing import Dict

from pydantic import BaseModel, Field

from fortigate_api.types_ import DAny


class Schema(BaseModel):
    """App/model data, URL to object, etc."""

    path: str = Field(default="", description="Path to object")
    uid: str = Field(default="", description="UID key of object")
    w_uid: DAny = Field(default={}, description="Schema for path with UID")
    wo_uid: DAny = Field(default={}, description="Schema for path without UID")


DSchema = Dict[str, Schema]
