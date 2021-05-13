from covid import app


@app.route("/")
def elnombrequemasrabiatede():
    return "Flask está funcionando desde views!"