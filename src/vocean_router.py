from flask import Flask
from get_symbols.bibox_symbols import get_symbol_json
from db_tools.read_from_db import read_symbol_from_db

app = Flask(__name__)


@app.route("/")
def hello():
    return read_symbol_from_db().to_json()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=1507)
