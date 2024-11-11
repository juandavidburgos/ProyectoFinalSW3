#Aplicacion principal
from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)
app.secret_key = 'flask'

@app.route('/')
def index():
    return print("Hola Bellas")
if __name__ == '__main__':
    app.run(debug=True)