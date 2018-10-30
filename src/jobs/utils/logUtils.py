from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy.ext.declarative import declarative_base
from config import DBInfo
import datetime

Base = declarative_base()


class LogInfo(Base):
    __tablename__ = 'log_info'
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    log_time = Column(DateTime, nullable=False)
    symbol = Column(String(200), nullable=False)
    start_time = Column(DateTime, nullable=True)
    end_time = Column(DateTime, nullable=True)
    start_id = Column(BigInteger, nullable=True)
    end_id = Column(BigInteger, nullable=True)
    new_record_count = Column(Integer, nullable=True)
    message = Column(String(200), nullable=False)

    def add_new_log(self, conn):
        e = conn
        Base.metadata.create_all(e)
        s = Session(e)

        s.add(self)
        s.flush()
        s.commit()
        print(self.id)


if __name__ == "__main__":
    time_now = datetime.datetime.now()
    print(time_now)
    msg = f"insert data successful at {time_now}."
    updateRecord = LogInfo(log_time=time_now,
                           start_time=time_now,
                           end_time=time_now,
                           start_id=110,
                           end_id=111,
                           overlap_count=23,
                           message=msg)
    updateRecord.add_new_log(DBInfo.conn)
