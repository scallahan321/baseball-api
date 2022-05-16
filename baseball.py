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
    start_year = request.args.get('start-year')
    start_month = request.args.get('start-month')
    start_day = request.args.get('start-day')
    end_year = request.args.get('end-year')
    end_month = request.args.get('end-month')
    end_day = request.args.get('end-day')
    start_date = start_year + '-' + start_month + '-' + start_day
    if not end_year:
        data = statcast_with_spin(start_date)
    else:
        end_date = end_year + '-' + end_month + '-' + end_day
        data = statcast_with_spin(start_date, end_date)
    data.to_csv("static/new_data.csv", index=False)
    return send_file("./static/new_data.csv", as_attachment=False)

