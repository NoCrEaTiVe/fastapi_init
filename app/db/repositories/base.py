from app.db.database import async_session as session


class BaseRepository:
    def __init__(self, db_session: session):
        self.db_session = db_session

    @property
    def connection(self):
        return self.db_session
