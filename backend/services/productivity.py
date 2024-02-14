"""Stand-in data layer until we connect to the database.

This file provides some overly simplistic access functions to support the minimum
API of this exercise. Ultimately, functions like these will be backed by an actual
storage system such as a relational database.
"""

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
            Exception: Timer does not exist.
        """
        global _timers
        if timer_id not in _timers:
            raise Exception(f"Invalid ID {timer_id}: Timer does not exist.")
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
            timer: Timer to modify.
        Returns:
            PomodoroTimer: Updated timer.
        Raises:
            Exception: Timer does not exist.
        """
        global _timers
        if timer.id not in _timers:
            raise Exception(
                f"Invalid ID {timer.id}: Cannot edit a timer that does not exist."
            )
        _timers[timer.id] = timer
        return timer

    def delete_timer(self, timer_id: int) -> None:
        """Deletes one timer from the data store.

        Args:
            timer_id: ID of the timer to delete.
        Raises:
            Exception: Timer does not exist.
        """
        global _timers

        if timer_id not in _timers:
            raise Exception(f"Could not delete a timer that does not exist.")
        del _timers[timer_id]
