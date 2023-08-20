#!/usr/bin/env python3
"""Module to Get Locale from request"""
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
    """Returns the locale from request"""
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route("/")
def display_basic_page():
    """Displays a simple page to test Babel connection"""
    return render_template("2-index.html")


if __name__ == "__main__":
    app.run()
