"""
AutoPoster - Post Model
"""
from sqlalchemy import Column, Integer, String, Text, DateTime, Boolean, JSON, ForeignKey, Enum
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
import enum
from app.core.database import Base

class PostStatus(enum.Enum):
    DRAFT = "draft"
    SCHEDULED = "scheduled"
    PUBLISHED = "published"
    FAILED = "failed"

class Post(Base):
    __tablename__ = "posts"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    title = Column(String(255))
    content = Column(Text)
    media_urls = Column(JSON, default=list)  # Image/video URLs
    status = Column(Enum(PostStatus), default=PostStatus.DRAFT)
    scheduled_at = Column(DateTime(timezone=True), nullable=True)
    published_at = Column(DateTime(timezone=True), nullable=True)
    platforms = Column(JSON, default=list)  # ["twitter", "linkedin", "zhihu"]
    metadata = Column(JSON, default=dict)  # Platform-specific data
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    user = relationship("User", back_populates="posts")

class Platform(Base):
    __tablename__ = "platforms"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), unique=True)  # twitter, linkedin, zhihu, etc.
    display_name = Column(String(100))
    icon = Column(String(100))  # Icon name
    enabled = Column(Boolean, default=True)
    config_schema = Column(JSON, default=dict)  # Platform config fields
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class ScheduledTask(Base):
    __tablename__ = "scheduled_tasks"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    post_id = Column(Integer, ForeignKey("posts.id"))
    platform = Column(String(50))
    cron_expression = Column(String(100))  # Cron expression
    enabled = Column(Boolean, default=True)
    last_run = Column(DateTime(timezone=True), nullable=True)
    next_run = Column(DateTime(timezone=True), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())