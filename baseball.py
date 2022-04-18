from flask import Flask
from dotenv import load_dotenv
from pybaseball import statcast

load_dotenv()

app = Flask(__name__)

@app.route("/")
def hello_world():

    # data = statcast('2022-04-01', '2022-04-18')
    # test = {}
    # test['value'] = data['pitch_type'].iloc[0]

    return ("Hi sean")