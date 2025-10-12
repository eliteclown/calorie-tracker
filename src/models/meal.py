from sqlalchemy import Integer,string,Float,ForeignKey
from sqlalchemy.orm import relationship
from src.db.session import Base
from datetime import datetime,date


class Meal(Base):
    id=Column(Integer,primary_key=True,index=True)
    user_id=Column(Integer,ForiegnKey("users.id"),nullable=False)
    log_date=Column(Date,nullable=False)
    meal_type=Column(String(50),nullable=False)

    
    user =relationship("User",back_populates="meals")
    items= relationship("MealItem",back_populates="meal")