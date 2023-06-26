from flask import Flask
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
csrf = CSRFProtect(app)
message = "Solution Sprint - Fase 05 - Pedro & Plínio"

@app.route("/")
def pagina_inicial():
    return message

@app.route('/bug')                                                                                                                                
def bad():                                                                                                                                        
    try:                                                                                                                                          
        raise TypeError()                                                                                                                         
    except TypeError as e:                                                                                                                        
        print(e)                                                                                                                                  
    except TypeError as e:                                                                                                                        
        print("Duplicado, ou seja, nunca vai entrar aqui.")