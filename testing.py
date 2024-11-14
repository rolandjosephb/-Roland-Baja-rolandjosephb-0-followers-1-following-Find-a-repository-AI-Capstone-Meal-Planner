
from flask import Flask


app = Flask(__name__)


@app.route("/")
def whatever():
    return "the output"


@app.route("/2")
def whatever2():
    return "the output2 for url with 2"

if __name__ == '__main__':
    app.run(debug=True)