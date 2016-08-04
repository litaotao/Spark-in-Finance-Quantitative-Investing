# -*- coding: utf-8 -*-

import sys
import time
import json

import pandas as pd
from flask import Flask
from flask.ext.restful import Api, Resource
from flask import Flask, request, send_file, Response, render_template



app = Flask(__name__, static_folder='./static', template_folder='./templates')
app.secret_key = 'ok, do u l0ve me ~^_ '
api = Api(app)


def get_line_data():
    _dict = json.load(file('logs/data-2016-08-04T13-03-18.json', 'r'))
    df = pd.DataFrame.from_dict(_dict)

    return df


class Main(Resource):
    def get(self): 
        df = get_line_data()

        change_1 = [0.0,0.0059861479,0.0052151855,0.0035916257,0.0026230372,0.0024244655,0.0027056178,0.0027264206,0.0026744137,0.002337157,0.0017751677,]
        bar_time = list(df.minute)
        bar_time = [str(i) for i in bar_time]


        return Response(render_template('display.html', barTime=bar_time,
            change_1=change_1, 
            change_2=change_1, 
            change_3=change_1, 
            ))


api.add_resource(Main, '/')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
