from fastapi import FastAPI 
from sqlalchemy import inspect, text
from src.db.session import engine , Base
from src.models import User , Food , Meal , MealItem ,Activity
from src.routers import foods,meals,auth_routes,activities

# Ensure all tables exist
Base.metadata.create_all(bind=engine)

# Ensure expected columns exist on existing tables (for environments without migrations)
inspector = inspect(engine)
existing_columns = {col["name"] for col in inspector.get_columns("meal_items")}
required_columns = ["calories", "protein", "carbs", "fat"]
missing_columns = [c for c in required_columns if c not in existing_columns]
if missing_columns:
    with engine.begin() as conn:
        for column_name in missing_columns:
            # Using DOUBLE to align with SQLAlchemy Float default on MySQL
            conn.execute(text(f"ALTER TABLE meal_items ADD COLUMN {column_name} DOUBLE NULL"))

app = FastAPI(title="Calorie-Tracker")

app.include_router(foods.router)
app.include_router(meals.router)
app.include_router(auth_routes.router)
app.include_router(activities.router)