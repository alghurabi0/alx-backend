#!/usr/bin/env python3
"""Flask application"""
from flask import Flask, render_template


app = Flask(__name__)

@app.route("/")
def home():
    """home page route handler"""
    return render_template("0-index.html")

if __name__ == "__main__":
    """init of script"""
    app.run()
