"""Productivity API

Productivity routes are used to create, retrieve, and update Pomodoro timers."""

from fastapi import APIRouter, Depends
from ..models.pomodorotimer import PomodoroTimer
from ..services.productivity import ProductivityService

__authors__ = ["Ajay Gandecha"]
__copyright__ = "Copyright 2024"
__license__ = "MIT"

api = APIRouter(prefix="/api/productivity")
openapi_tags = {
    "name": "Productivity",
    "description": "Create, update, delete, and retrieve Pomodoro timers.",
}


@api.get("", response_model=list[PomodoroTimer], tags=["Productivity"])
def get_timers(
    productivity_service: ProductivityService = Depends(),
) -> list[PomodoroTimer]:
    """
    Get all pomodoro timers.

    Parameters:
        productivity_service: a valid ProductivityService

    Returns:
        list[PomodoroTimer]: All pomodoro timers
    """

    # Return all pomodoro timers
    return productivity_service.get_timers()


@api.post("", response_model=PomodoroTimer, tags=["Productivity"])
def create_timer(
    timer: PomodoroTimer,
    productivity_service: ProductivityService = Depends(),
) -> PomodoroTimer:
    """
    Create pomodoro timer.

    Parameters:
        timer: a valid PomodoroTimer model
        productivity_service: a valid ProductivityService

    Returns:
        PomodoroTimer: Created pomodoro timer
    """

    return productivity_service.create_timer(timer)


@api.put("", response_model=PomodoroTimer, tags=["Productivity"])
def update_timer(
    timer: PomodoroTimer,
    productivity_service: ProductivityService = Depends(),
) -> PomodoroTimer:
    """
    Update pomodoro timer.

    Parameters:
        timer: a valid PomodoroTimer model
        productivity_service: a valid ProductivityService

    Returns:
        PomodoroTimer: Updated pomodoro timer
    """

    return productivity_service.update_timer(timer)


@api.delete("/{id}", response_model=None, tags=["Productivity"])
def delete_timer(
    id: int,
    productivity_service: ProductivityService = Depends(),
) -> PomodoroTimer:
    """
    Delete pomodoro timer.

    Parameters:
        id: ID of the timer to delete
        productivity_service: a valid ProductivityService
    """

    return productivity_service.delete_timer(id)
