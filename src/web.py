"""
    Web application start script
"""

from .app import careate_app

app = careate_app()

app.run(debug=False, host='0.0.0.0')
