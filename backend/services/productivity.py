"""Stand-in data layer until we connect to the database.

This file provides some overly simplistic access functions to support the minimum
API of this exercise. Ultimately, functions like these will be backed by an actual
storage system such as a relational database.
"""

from fastapi import HTTPException
from ..models.pomodorotimer import PomodoroTimer

__author__ = "Ajay Gandecha"
__copyright__ = "Copyright 2024"
__license__ = "MIT"

_timer_id = 1
_timers: dict[int, PomodoroTimer] = {}
"""Private module data simulating a simple key-value store where keys are the timer ID and values are timer objects. Do not reference externally."""


class ProductivityService:
    """Backend service that enables direct modification of pomodoro timer data."""

    def reset(self):
        """Resets all pomodoro timer data"""
        global _timers
        _timers = {}

    def get_timers(self) -> list[PomodoroTimer]:
        """
        Retrieves all pomodoro timers.

        Returns:
            list[PomodoroTimer]: All pomodoro timer data.
        """
        global _timers
        return _timers.values()

    def get_timer(self, timer_id: int) -> PomodoroTimer:
        """Gets one timer by an ID.

        Args:
            timer_id: Timer to retieve.
        Returns:
            PomodoroTimer: Timer with the matching ID.
        Raises:
            HTTPException: Timer does not exist.
        """
        global _timers
        if timer_id not in _timers:
            raise HTTPException(
                status_code=404, detail=f"Invalid ID {timer_id}: Timer does not exist."
            )
        return _timers[timer_id]

    def create_timer(self, timer: PomodoroTimer) -> PomodoroTimer:
        """Stores a timer in the data store.

        Args:
            timer: Timer to store.
        Returns:
            PomodoroTimer: Created timer.
        """
        global _timers, _timer_id
        timer.id = _timer_id
        _timers[_timer_id] = timer
        _timer_id += 1
        return timer

    def update_timer(self, timer: PomodoroTimer) -> PomodoroTimer:
        """Modifies one timer in the data store.

        Args:
            timer: Data for a timer with modified values.
        Returns:
            PomodoroTimer: Updated timer.
        Raises:
            HTTPException: Timer does not exist.
        """
        # TODO: Implement this service function. To do this successfully, you must:
        # - Update the correct timer in the backend.
        # - Throw the correct exception if the user tries to edit a timer that does not exist.
        # - Return the updated timer.

    def delete_timer(self, timer_id: int) -> None:
        """Deletes one timer from the data store.

        Args:
            timer_id: ID of the timer to delete.
        Raises:
            HTTPException: Timer does not exist.
        """
        global _timers

        if timer_id not in _timers:
            raise HTTPException(
                status_code=404, detail=f"Invalid ID {timer_id}: Timer does not exist."
            )
        del _timers[timer_id]
