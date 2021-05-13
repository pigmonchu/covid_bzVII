from flask import Flask

app = Flask(__name__)

@app.route("/")
def elnombrequemasrabiatede():
    return "Flask está funcionando!"