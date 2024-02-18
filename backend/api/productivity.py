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

# TODO: Implement the following API:
# GET /api/productivity
# Gets all pomodoro timers.
# Expected return type: list[PomodoroTimer]


# TODO: Implement the following API:
# GET /api/productivity/{id}
# Get a pomodoro timer by its ID.
# Expected return type: PomodoroTimer


# TODO: Implement the following API:
# POST /api/productivity/
# Creates a new pomodoro timer.
# Note: This API will take in a request body. What type should this be?
# Expected return type: PomodoroTimer


# TODO: Implement the following API:
# PUT /api/productivity
# Updates a pomodoro timer.
# Note: This API will take in a request body. What type should this be?
# Expected return type: PomodoroTimer


# TODO: Implement the following API:
# DELETE /api/productivity/{id}
# Deletes a pomodoro timer.
# Expected return type: PomodoroTimer
