import logging

from flask import Blueprint, render_template, send_from_directory

log = logging.getLogger(__name__)
main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template("index.html")


@main.route('/static/<path:path>')
def send_js(path):
    return send_from_directory('static', path)
