#!/usr/bin/env python3
"""Flask app
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"}
}


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


def get_user():
    """
    return user if found
    """
    user_id = request.args.get('login_as')
    if user_id:
        return users.get(int(user_id))
    return None


@app.before_request
def before_request() -> None:
    """
    execute first
    """
    user = get_user()
    g.user = user


@babel.localeselector
def get_locale() -> str:
    """
    determines the best match and get local selector
    """
    query = request.args.get('locale', None)
    if query and query in app.config['LANGUAGES']:
        return query
    if g.user:
        query = g.user.get('locale')
        if query in app.config['LANGUAGES']:
            return query
    query = request.headers.get('locale', '')
    if query and query in app.config["LANGUAGES"]:
        return query
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@babel.timezoneselector
def get_timezone() -> str:
    """
    time zone selector
    """
    tzone = request.args.get('timezone', '').strip()
    if not tzone and g.user:
        tzone = g.user['timezone']
    try:
        return pytz.timezone(tzone).zone
    except pytz.exceptions.UnknownTimeZoneError:
        return app.config['BABEL_DEFAULT_TIMEZONE']


@app.route('/', strict_slashes=False)
def get_index() -> str:
    """
    creates / route and index.html template
    """
    return render_template('6-index.html')
