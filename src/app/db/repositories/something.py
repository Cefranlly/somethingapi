from app.db.repositories.base import BaseRepository
from app.models.something import SomethingCreate, SomethingInDB, SomethingAll


CREATE_SOMETHING_QUERY = """
    INSERT INTO interview_table (tracker_uuid, exchange_uuid, start_time, original_utterance, asr_truth, duration, responses)
    VALUES (:tracker_uuid, :exchange_uuid, :start_time, :original_utterance, :asr_truth, :duration, :responses)
    RETURNING (tracker_uuid, exchange_uuid, start_time, original_utterance, asr_truth, duration, responses);
"""

DELETE_SOMETHING_QUERY = """
    DELETE FROM interview_table WHERE tracker_uuid = :tracker_uuid;
"""

GET_ALL_SOMETHING_QUERY = """
    SELECT * FROM interview_table limit 10;
"""

class SomethingRepository(BaseRepository):
    """"
    All database actions associated with the resource
    """

    async def create_something(self, *, new_something: SomethingCreate) -> SomethingInDB:
        query_values = new_something.dict()
        something = await self.db.fetch_one(query=CREATE_SOMETHING_QUERY, values=query_values)
        # TODO: Check why the DB answer is not returning the values inserted
        return SomethingInDB(**something)

    async def get_all_something(self) -> SomethingAll:
        something = await self.db.fetch_all(query=GET_ALL_SOMETHING_QUERY)
        return SomethingAll(something)
