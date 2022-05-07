from flask import Flask, render_template
from flask import request
from search_files import *

app=Flask(__name__)

@app.route('/')
def home():
    
    return render_template('public_html.html')
@app.route('/results')
def results():
    word=request.args.get('word')
    results=searchWord(word)
    html=' '
    for result in results:
        
        html+=('<a href="/document/'+result[3:]+'"><h2>'+result+'</h2></a>')
    return "<h1>Retrieve "+word+"</h1><br>"+"<h1>Top Documents</h><br>" +html

@app.route('/document/<name>')
def loadLink(name):
    
    return render_template(name)

if __name__ == '__main__':
    app.run(debug=True)