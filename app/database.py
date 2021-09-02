import logging
from sqlalchemy import create_engine
from sqlalchemy.future import Engine
from sqlalchemy.exc import ProgrammingError
from sqlalchemy.sql import text
from app import DATABASE_URI
from app.core.exceptions import QueryExecutionFailException

logger = logging.getLogger(__name__)


class Database:
    @classmethod
    def _get_engine(cls) -> Engine:
        """
        create a engine with database info and return Engine instance
        """
        engine = create_engine(DATABASE_URI)
        return engine

    @classmethod
    def execute_query(cls, query):
        try:
            engine: Engine = cls._get_engine()
            return engine.execute(query)
        except ProgrammingError as error:
            logger.error(str(error))
            raise QueryExecutionFailException(details="System execution failed, try after some time.")
