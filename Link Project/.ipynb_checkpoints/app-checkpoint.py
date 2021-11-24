from flask import Flask, render_template
import webbrowser
import string, random
import pandas as pd
# df = pd('')

app = Flask(__name__)

@app.route('/<name>')
def index(name):
    print('The number of ',dict_links[name][0])
    # webbrowser.open(dict_links[name][0])


@app.route('/')
def home(): 
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)