from sqlalchemy import Integer,String,Float,ForeignKey
from sqlalchemy.orm import relationship
from src.db.session import Base

class MealItem(Base):
    __tablename__="meal_items"

    id=Column(Integer,primary_key=True,index=True)
    meal_id=Column(Integer,ForeignKey("meals.id"),nullable=False)
    food_id=Column(Integer,ForeignKey("foods.id"),nullable=False)
    quantity=Column(Float,nullable=False)
    protein=Column(Float)
    carbs=Column(Float)
    fat=Column(Float)

    meal = relationship("Meal",back_populates="items")
    food = relationship("Food")