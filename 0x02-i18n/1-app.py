#!/usr/bin/env python3
"""Basic Babel setup"""
from flask import (render_template, Flask)
from flask_babel import Babel


class Config:
    """Configures available languages in our app"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
babel = Babel(app)
app.config.from_object(Config)


@app.route("/")
def display_basic_page():
    """Displays a simple page to test Babel setup"""
    return render_template("1-index.html")


if __name__ == "__main__":
    app.run()
