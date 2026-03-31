from flask import Flask 
from database import criar_tabelas

criar_tabelas()

app = Flask(__name__)

from rotas import *

if __name__=='__main__':
    app.run(debug=True)