from flask import Flask, render_template, request, redirect, url_for
import time
import csv 
from datetime import datetime
import pandas as pd

app = Flask(__name__)

PORT=5000

@app.route('/', methods=['GET', 'POST'])
def root():
	return render_template('index.html')
    


@app.route('/marks', methods=['GET', 'POST'])
def index():
	return render_template('index.html')


@app.route('/getdetails', methods=['GET', 'POST'])
def getdetails():
    if request.method == 'POST':
        name = request.form['name']
        date = request.form['date']
        date=str(date)
        
    
    result = { 
        'Event Name': name,
        'Date': date 
    }

    df = pd.DataFrame([result.values()], columns=['Event Name', 'Date'])
    df.to_csv('event.csv', mode='a', header=False, index=False)
        
              
              
    return redirect(url_for('index')) 
        
    # df = pd.read_csv('event.csv')
    # df.append({'Event Name': name, 'Date': date },ignore_index=True)
        
  

    # df.to_csv('event.csv', header=True, index=False)
    # print(df)

    # return render_template('new.html',df=df.to_csv('event.csv',header=True,index=False))  

if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port=PORT)