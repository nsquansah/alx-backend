#!/usr/bin/env python3
"""Module to Force locale with URL Parameter"""
from flask import (render_template, request, Flask)
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


@app.route("/")
def display_basic_page():
    """Displays a simple page to test Babel connection"""
    return render_template("4-index.html")


if __name__ == "__main__":
    app.run()
