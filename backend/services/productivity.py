"""Stand-in data layer until we connect to the database.

This file provides some overly simplistic access functions to support the minimum
API of this exercise. Ultimately, functions like these will be backed by an actual
storage system such as a relational database.
"""

from ..models.pomodorotimer import PomodoroTimer

__author__ = "Ajay Gandecha"
__copyright__ = "Copyright 2024"
__license__ = "MIT"

_timers: dict[int, PomodoroTimer] = {}
"""Private module data simulating a simple key-value store where keys are the timer ID and values are timer objects. Do not reference externally."""


class ProductivityService:
    def reset(self):
        global _timers
        _timers = {}

    def get_timers(self) -> list[PomodoroTimer]:
        global _timers
        return _timers.values()

    def create_timer(self, timer: PomodoroTimer) -> PomodoroTimer:
        global _timers
        if timer.id in _timers:
            raise Exception(f"Invalid ID {timer.id}: ID already exists.")

        _timers[timer.id] = timer
        return timer

    def update_timer(self, timer: PomodoroTimer) -> PomodoroTimer:
        global _timers
        if timer.id not in _timers:
            raise Exception(
                f"Invalid ID {timer.id}: Cannot edit a timer that does not exist."
            )
        _timers[timer.id] = timer
        return timer

    def delete_timer(self, timer_id: int) -> None:
        global _timers

        if timer_id not in _timers:
            raise Exception(f"Could not delete a timer that does not exist.")
        del _timers[timer_id]
