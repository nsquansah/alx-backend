#!/usr/bin/env python3
"""Module to handle locale based on several factors priority factors"""
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


#@babel.localeselector
def get_locale():
    """Returns the locale requested based on several priorities"""

    supported_langs = app.config["LANGUAGES"]
    # Handling priority 1: Locale from URL parameters
    url_locale = request.args.get("locale")
    if url_locale is not None and url_locale in supported_langs:
        return url_locale
    # Handling priority 2: Locale from user settings
    if g.user is not None:
        user_set = g.user.get("locale")
        if user_set is not None and user_set in supported_langs:
            print("Req - Header2")
            return user_set
    # Handling priority 3: Locale from request header
    req_header = request.accept_languages.best_match(app.config["LANGUAGES"])
    if req_header is not None:
        print("Req - Header3")
        return req_header

    # Handling priority 4: Default Locale
    return app.config["BABEL_DEFAULT_LOCALE"]


babel.init_app(app, locale_selector=get_locale)


@app.route("/")
def display_basic_page():
    """Displays a simple page to test Babel connection"""
    return render_template("6-index.html")


if __name__ == "__main__":
    app.run(debug=True)
