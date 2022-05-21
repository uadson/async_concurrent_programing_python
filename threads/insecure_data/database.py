from tkinter import SW
import warnings

from sqlalchemy.exc import SAWarning
from sqlmodel.sql.expression import Select, SelectOfScalar

from sqlmodel import create_engine, Session

from insecure_data import models
from insecure_data.config import url


warnings.filterwarnings('ignore', category=SAWarning)
SelectOfScalar.inherit_cache = True
Select.inherit_cache = True

engine = create_engine(url, echo=False)
models.SQLModel.metadata.create_all(engine)


def get_session():
    return Session(engine)
