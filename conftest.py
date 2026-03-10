import asyncio

import pytest

pytest_plugins = [
    "tests.fixtures.users.user_repository",
    "tests.fixtures.auth.auth_service",
    "tests.fixtures.auth.clients",
    "tests.fixtures.infrastructure",
]
