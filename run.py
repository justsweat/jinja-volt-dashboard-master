# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from app import app


if __name__ == '__main__':
    app.run(debug=True, port=8000, host='127.0.0.1')
