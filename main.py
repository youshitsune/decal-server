from flask import Flask
from flask import request

app = Flask(__name__)

with open("cal.txt", "r") as f:
    ctx = [i for i in f.read().split("-") if i]

for i in range(len(ctx)):
    ctx[i] = [i for i in ctx[i].splitlines() if i]

@app.route("/", methods=["POST"])
def index():
    if request.get_json()["pass"] == "<password_here>":
        return ctx
    else:
        return "Wrong password"

app.run()
