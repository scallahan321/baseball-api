from flask import Flask, request, send_file
from dotenv import load_dotenv
#from pybaseball import statcast
from spin import statcast_with_spin

load_dotenv()


app = Flask(__name__)

@app.route("/")
def hello_world():

    return "Hello World"


@app.route("/get_data")
def get_csv_attachment():
    data = statcast_with_spin('2022-04-18')
    data.to_csv("static/new_data.csv", index=False)
    return send_file("./static/new_data.csv", as_attachment=False)

# @app.route("/get_csv")
# def get_csv():
#     csv_path = "./static/sample1.csv"
#     return send_file(csv_path, as_attachment=False)