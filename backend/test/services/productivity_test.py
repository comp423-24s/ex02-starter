"""Tests for the mock storage layer."""

from ...services.productivity import ProductivityService
from ...models.pomodorotimer import PomodoroTimer
import pytest


@pytest.fixture(autouse=True)
def productivity_service():
    """This PyTest fixture is injected into each test parameter of the same name below.

    It constructs a new, empty StorageService object."""
    productivity_service = ProductivityService()
    productivity_service.reset()
    return productivity_service


def test_get_timers_empty(productivity_service: ProductivityService):
    assert len(productivity_service.get_timers()) == 0


def test_add_timer(productivity_service: ProductivityService):
    timer = PomodoroTimer(
        id=1, name="Sample", description="Description", timer_length=10, break_length=5
    )
    result = productivity_service.create_timer(timer)
    assert result is not None
    assert timer.id == result.id
    assert len(productivity_service.get_timers()) == 1


def test_add_timer_already_exists(productivity_service: ProductivityService):
    timer = PomodoroTimer(
        id=1, name="Sample", description="Description", timer_length=10, break_length=5
    )
    productivity_service.create_timer(timer)
    second_timer = PomodoroTimer(
        id=1, name="Another", description="Description", timer_length=10, break_length=5
    )
    with pytest.raises(Exception):
        productivity_service.create_timer(second_timer)


def test_get_timer(productivity_service: ProductivityService):
    timer = PomodoroTimer(
        id=1, name="Sample", description="Description", timer_length=10, break_length=5
    )
    productivity_service.create_timer(timer)
    result = productivity_service.get_timer(timer.id)
    assert result is not None
    assert timer.id == result.id


def test_get_timer_none_exists(productivity_service: ProductivityService):
    with pytest.raises(Exception):
        productivity_service.get_timer(1)


# TODO: Implement two tests for updating a timer.


def test_delete_timer(productivity_service: ProductivityService):
    timer = PomodoroTimer(
        id=1, name="Sample", description="Description", timer_length=10, break_length=5
    )
    result = productivity_service.create_timer(timer)
    before_length = len(productivity_service.get_timers())

    productivity_service.delete_timer(timer.id)
    after_length = len(productivity_service.get_timers())

    assert after_length == before_length - 1


def test_delete_timer_none_exists(productivity_service: ProductivityService):
    with pytest.raises(Exception):
        productivity_service.delete_timer(1)
