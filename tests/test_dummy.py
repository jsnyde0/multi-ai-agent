import pytest


@pytest.fixture
def dummy_fixture():
    return True


def test_dummy(dummy_fixture):
    """A simple test to verify pytest is working."""
    assert dummy_fixture
    