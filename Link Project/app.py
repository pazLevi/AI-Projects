from flask import Flask, render_template
import webbrowser
import string, random
import pandas as pd

df = pd.read_json('data.json').set_index('New link')

app = Flask(__name__)

@app.route('/<name>')
def index(name):
    df.loc[name]['Counter'] += 1
    print('Number of entries:',df.loc[name]['Counter'])
    webbrowser.open(df.loc[name]['Original link'])


# @app.route('/')
# def home(): 
#     return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)