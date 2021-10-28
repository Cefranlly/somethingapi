from typing import Optional, List

from app.models.core import CoreModel


class SomethingBase(CoreModel):
    """
    All common characteristics of our resource
    """
    tracker_uuid: Optional[str]
    exchange_uuid: Optional[str]
    start_time: Optional[str]
    original_utterance: Optional[str]
    asr_truth: Optional[str]
    duration: Optional[float]
    responses: Optional[str]


class SomethingCreate(SomethingBase):
    tracker_uuid: str
    exchange_uuid: str
    start_time: str
    original_utterance: str
    duration: float
    responses: str


class SomethingUpdate(SomethingBase):
    pass


class SomethingInDB(SomethingBase):
    pass


class SomethingPublic(SomethingBase):
    pass


class SomethingAll(CoreModel):
    result: List[SomethingBase]
