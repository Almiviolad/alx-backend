#!/usr/bin/env python3
""" Flask app module tha prints welcome message"""
from flask import Flask, render_template
from typing import Any
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """configure available languages"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_TIMEZONE = 'UTC'
    BABEL_DEFAULT_LOCALE = 'en'


app.config.from_object(Config)

@babel.localeselector
def get_locale():
    """determine the best match with our supported languages"""
    request.accept_languages.best_match(app.config['LANGUAGES'])

@app.route('/')
def home() -> Any:
    """outputs welcome message"""
    return render_template('2-index.html')


if __name__ == '__main__':
    app.run()
