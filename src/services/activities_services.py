from sqlalchemy.orm import Session
from src.models.activity import Activity
from src.schemas import activity_dto

def create_activity(db:Session , user_id:int , activity:activity_dto.ActivityCreate):
    db_act = Activity(
        user_id = user_id,
        name = activity.name,
        calories_burned = activity.calories_burned,
        activity_time = activity.activity_time
    )


    db.add(db_act)
    db.commit()
    db.refresh(db_act)
    return db_act


def get_activities_for_user(db:Session,user_id:int):
    return db.query(Activity).filter(Activity.user_id == user_id).all()