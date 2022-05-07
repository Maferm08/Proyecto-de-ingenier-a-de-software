from flask import Flask, render_template
from flask import request
from search_files import *
import cgi
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
        html+=('<h2>'+result+'</h2>')

    
    # return render_template('results.html')
    return html
if __name__ == '__main__':
    app.run(debug=True)