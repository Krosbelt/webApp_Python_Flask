#Import flask
from flask import Flask, render_template

#import request to be able to request data to the api
import requests

#Iniciando la aplicación
app = Flask(__name__)


#route
@app.route('/')
def index():  #Function that allows access to data
    datosObtenidos = requests.get('https://api.dailymotion.com/videos?channel=sport&limit=10') #request data to the api
    datosFormatJSON = datosObtenidos.json() #convert data to json format
    print(datosFormatJSON)
    
    return render_template('index.html', datos=datosFormatJSON['list'])

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
