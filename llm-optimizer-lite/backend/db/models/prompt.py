from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from backend.db.base import Base


class PromptTemplate(Base):
    __tablename__ = "prompt_templates"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(120), unique=True)
