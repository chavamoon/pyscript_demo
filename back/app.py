# importing flask
from flask import Flask, render_template
 
# importing pandas module
import pandas as pd
import os
 
template_dir = os.path.abspath('../front/views/')
static_files_dir = os.path.abspath('../front/assets/')
app = Flask(__name__, template_folder= template_dir, static_folder=static_files_dir)


@app.route('/')
def index():
     return render_template('index.html')
 
# # route to html page - "table"
@app.route('/table')
def table():
 # converting csv to html
    data = pd.read_csv('https://raw.githubusercontent.com/rishabh89007/Time_Series_Datasets/main/Cali%20Emissions.csv', index_col=0)
    return data.to_json()
 
 
if __name__ == "__main__":
     app.run(host='localhost',port=int(5005))