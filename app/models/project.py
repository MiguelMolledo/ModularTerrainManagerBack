from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.sql import func
from sqlalchemy import Column, Integer, String, DateTime
from app.database.base_class import Base


class Project(Base):
    __tablename__ = "projects"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now())

    def __repr__(self):
        return f"<Project(Id={self.id}, name={self.name})>"
