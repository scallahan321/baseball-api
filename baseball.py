from flask import Flask, request, send_file
from dotenv import load_dotenv
from spin import statcast_with_spin
from datetime import date
from datetime import timedelta

load_dotenv()




app = Flask(__name__)

@app.route("/")
def hello_world():

    return "Hello World"


@app.route("/get_data")
def get_csv_attachment():
    today = date.today()
    yesterday = today - timedelta(days = 1)
    #data = statcast_with_spin('2022-04-18')
    data = statcast_with_spin(str(yesterday))
    data.to_csv("static/new_data.csv", index=False)
    return send_file("./static/new_data.csv", as_attachment=False)

