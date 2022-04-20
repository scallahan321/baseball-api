from pybaseball import statcast

data = statcast('2022-04-19')

data.to_csv("static/data.csv")