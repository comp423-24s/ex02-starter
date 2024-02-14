"""Model for Pomodoro Timer data."""

from datetime import datetime
from pydantic import BaseModel


class PomodoroTimer(BaseModel):
    id: int
    name: str
    description: str
    timer_length: int
    break_length: int
