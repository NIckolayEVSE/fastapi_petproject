from sqlalchemy import select

from database import async_session_maker


class BaseService:
    model = None

    @classmethod
    async def find_by_id(cls, model_id: int):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(id=model_id)
            result = await session.execute(query)
            return result.mappings().one_or_none()

    @classmethod
    async def find_one_or_none(cls, **kwargs):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(**kwargs)
            result = await session.execute(query)
            return result.mappings().one_or_none()

    @classmethod
    async def find_all(cls, **kwargs):
        async with async_session_maker() as session:
            query = (
                select(cls.model)
                if not kwargs
                else select(cls.model).filter_by(**kwargs)
            )
            result = await session.execute(query)
            return result.mappings().all()

    @classmethod
    async def add(cls, **kwargs):
        async with async_session_maker() as session:
            # query = insert(cls.model).values(**kwargs)
            new_entry = cls.model(**kwargs)
            session.add(new_entry)
            await session.commit()
