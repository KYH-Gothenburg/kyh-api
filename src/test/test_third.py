"""
    Unit tests for first end-point
"""

import json
from .fixture import client

def test_third_status_code(client):
    """
    Test the api HTTP status code
    :param cleint: An app test client from the fixture
    :return: None
    """
    response = client.get('/api/v1.0/third')
    assert response.status_code == 200


def test_third_status_code(client):
    """
    Test the api returned data
    :param cleint: An app test client from the fixture
    :return: None
    """
    response = client.get('/api/v1.0/third')
    data = json.loads(response.text)
    assert data['name'] == 'Carla'
    