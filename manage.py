# -*- coding: utf-8 -*-
"""This module executes or application."""

from API import app


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)