"""Starter API for the Testing FastAPI with pytest assignment."""

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field

app = FastAPI(title="School Activities API")


class Activity(BaseModel):
    title: str = Field(min_length=1)
    subject: str = Field(min_length=1)
    completed: bool = False


class ActivityResponse(Activity):
    id: int


activities: list[ActivityResponse] = []
next_id = 1


@app.get("/health")
def health_check() -> dict[str, str]:
    """Return a simple response that confirms the API is running."""
    return {"status": "ok"}


@app.get("/activities", response_model=list[ActivityResponse])
def list_activities() -> list[ActivityResponse]:
    """Return every activity currently stored in memory."""
    return activities


@app.post(
    "/activities",
    response_model=ActivityResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_activity(activity: Activity) -> ActivityResponse:
    """Create an activity and assign it the next available identifier."""
    global next_id

    created_activity = ActivityResponse(id=next_id, **activity.model_dump())
    activities.append(created_activity)
    next_id += 1
    return created_activity


@app.get("/activities/{activity_id}", response_model=ActivityResponse)
def get_activity(activity_id: int) -> ActivityResponse:
    """Find one activity by identifier."""
    for activity in activities:
        if activity.id == activity_id:
            return activity

    raise HTTPException(status_code=404, detail="Activity not found")


@app.delete("/activities/{activity_id}")
def delete_activity(activity_id: int) -> dict[str, str]:
    """Remove an activity by identifier."""
    for index, activity in enumerate(activities):
        if activity.id == activity_id:
            activities.pop(index)
            return {"message": "Activity deleted"}

    raise HTTPException(status_code=404, detail="Activity not found")