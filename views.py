import json
import flask
from flask_cors import CORS
from computer_vision.process import process
from solver.solve import solveBoard

main = flask.Blueprint('main', __name__)
cors = CORS(main, resources={r"/api/*": {"origins": "*"}})


@main.route("/api/image/", methods=["POST"])
def process_image():
    try:
        picture = flask.request.json
        board = process(picture["data"])
        print("got board", board)
        return json.dumps(board)
    except Exception as e:
        return "Error"


@main.route("/api/solve/", methods=["POST"])
def solve():
    board = flask.request.json
    solutions = solveBoard(board["data"])
    return solutions


@main.route("/", methods=["GET"])
def test():
    return "Hello World"
