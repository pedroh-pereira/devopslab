from flask import Flask

app = Flask(__name__)

message = "Solution Sprint - Fase 05 - Pedro & Plínio"

@app.route("/")
def pagina_inicial():
    return message