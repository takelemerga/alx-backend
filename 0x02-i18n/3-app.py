#!/usr/bin/env python3
"""Flask app
"""
from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """
    flask babel configuration
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)

app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """
    determines the best match
    """
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route('/', strict_slashes=False)
def get_index() -> str:
    """
    creates / route and index.html template
    """
    return render_template('3-index.html')
