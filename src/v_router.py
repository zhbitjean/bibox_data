from flask import Flask, request
from flask_restful import Resource, Api
from flask import jsonify
import json
from db_tools.read_from_db import read_symbol_from_db, read_df_from_db
from flask_cors import CORS, cross_origin
from jobs.watch_jobs import watch_mark
from config import DBInfo

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
api = Api(app)


class HelloWorld(Resource):
    def get(self):
        return {'about': 'Hello World!'}


class SymbolList(Resource):
    def get(self):
        df = read_symbol_from_db()
        df['date'] = df['date'].astype('datetime64[ms]')
        print(df['date'])
        df_chart = df.copy()
        df_chart = df_chart[df_chart['Volume'] != '0']
        print("df_chart *************************")
        print(df_chart)
        df_chart_json = json.loads(df_chart.to_json())
        df_string = df.T.to_json()
        df_json = json.loads(df_string)
        mark_price = 0.34
        res_dict = watch_mark(mark_price)
        result = jsonify({
            "data": df_json,
            "chart_data": df_chart_json,
            "ratio": res_dict['ratio'],
            "mark_price": res_dict['mark_price'],
            "latest_price": res_dict['latest_price']
        })
        return result


class SymbolForChart(Resource):
    def get(self):
        df = read_symbol_from_db()
        df['date'] = df['date'].astype('datetime64[ms]')
        df_string = df.to_json()
        df_json = json.loads(df_string)
        result = jsonify({
            "data": df_json,
        })
        return result


class SymbolTrade(Resource):
    def get(self):
        df = read_df_from_db("bibox_trade", DBInfo.conn)
        # df['date'] = df['date'].astype('datetime64[ms]')
        df_string = df.to_json()
        df_json = json.loads(df_string)
        result = jsonify({
            "data": df_json,
        })
        return result


api.add_resource(HelloWorld, '/')
api.add_resource(SymbolList, '/symbol_list')
api.add_resource(SymbolForChart, '/symbol_chart')
api.add_resource(SymbolTrade, '/symbol_trade')


@app.route('/test', methods=['GET'])
def get_msg():
    return 'test message'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
