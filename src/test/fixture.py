"""
Fixture for tests
"""

import pytest
from ..app import careate_app


@pytest.fixture
def client():
    """
    Test fixture for api client
    :return: yields a test client
    """
    app = careate_app()
    app.config['TESTING'] = True

    with app.app_context():
        with app.test_client() as api_client:
            yield api_client
