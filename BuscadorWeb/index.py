from flask import Flask
from Activity13 import *
app=Flask(__name__)

@app.route('/')
def home():
    searchWord()
    return 'yep'
if __name__ == '__main__':
    app.run()