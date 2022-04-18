from flask import Flask, request, send_file
from dotenv import load_dotenv
from pybaseball import statcast

load_dotenv()

app = Flask(__name__)

@app.route("/")
def hello_world():

    # data = statcast('2022-04-01', '2022-04-18')
    # test = {}
    # test['value'] = data['pitch_type'].iloc[0]

    return "testing gcp to heroku api connection"


@app.route("/get_csv_attachment")
def get_csv_attachment():
    csv_path = "./static/sample1.csv"
    return send_file(csv_path, as_attachment=True, attachment_filename="sample1.csv")

@app.route("/get_csv")
def get_csv():
    csv_path = "./static/sample1.csv"
    return send_file(csv_path, as_attachment=False)