"""
Api main app
"""


import json
from flask import Flask, Response


def careate_app():
    """
        App factory function
    """

    app = Flask(__name__)

    @app.get('/api/v1.0/first')
    def first_get():
        data = {
            'name': 'Alice',
            'age': 34
        }

        return Response(json.dumps(data), 200, content_type='application/json')

    @app.get('/api/v1.0/second')
    def second_get():
        data = {
            'name': 'Bob',
            'age': 56
        }

        return Response(json.dumps(data), 200, content_type='application/json')

    @app.get('/api/v1.0/third')
    def third_get():
        data = {
            'name': 'Carla',
            'age': 21
        }

        return Response(json.dumps(data), 200, content_type='application/json')

    return app

if __name__ == '__main__':
    careate_app().run(port=5550)