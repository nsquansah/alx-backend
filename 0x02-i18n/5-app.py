#!/usr/bin/env python3
"""Module to Force locale with URL Parameter"""
from flask import (g, render_template, request, Flask)
from flask_babel import Babel


class Config:
    """Configures available languages in our app"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
babel = Babel(app)
app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """Returns the locale requested via the 'locale' parameter"""
    args = request.args.get("locale")
    supported_langs = app.config["LANGUAGES"]
    if args is not None and args in supported_langs:
        return args
    return request.accept_languages.best_match(app.config["LANGUAGES"])


# babel.init_app(app, locale_selector=get_locale)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user():
    """Returns information about a user as a dictionary containing
    mock user data
    """
    id = request.args.get("login_as", None)
    try:
        id = int(id)
    except (ValueError, TypeError):
        id = None
    user = users.get(id)
    return user


@app.before_request
def before_request():
    """Creates a global 'user' variable if the 'login_as' parameter was passed
    """
    user = get_user()
    g.user = user


@app.route("/")
def display_basic_page():
    """Displays a simple page to test Babel connection"""
    return render_template("5-index.html")


if __name__ == "__main__":
    app.run()
