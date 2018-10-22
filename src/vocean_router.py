from flask import Flask, request
from flask_restful import Resource, Api
from flask import jsonify
import json
from get_symbols.bibox_symbols import get_symbol_json
from db_tools.read_from_db import read_symbol_from_db
from flask_cors import CORS, cross_origin
from jobs.watch_jobs import watch_mark

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
api = Api(app)


class HelloWorld(Resource):
    def get(self):
        return {'about': 'Hello World!'}


class SymbolList(Resource):
    def get(self):
        df_string = read_symbol_from_db().to_json()
        df_json = json.loads(df_string)
        mark_price = 0.34
        res_dict = watch_mark(mark_price)
        result = jsonify({
            "data": df_json,
            "ratio": res_dict['ratio'],
            "mark_price": res_dict['mark_price'],
            "latest_price": res_dict['latest_price']
        })
        return result


api.add_resource(HelloWorld, '/')
api.add_resource(SymbolList, '/symbol_list')


@app.route('/test', methods=['GET'])
def get_msg():
    return 'test message'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=1507, debug=True)
