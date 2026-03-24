"""Pytest configuration for {{ project_name }} tests."""

from __future__ import annotations

from typing import Generator

import pytest


@pytest.fixture(autouse=True)
def set_up_and_tear_down() -> Generator[None, None, None]:
    """Set up and tear down the test environment."""
    yield
    # Teardown code here