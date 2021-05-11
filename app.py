from flask import Flask, render_template, request
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
    global name
    if request.method == 'POST':
        name = request.form['name']
        date = request.form['date']
        date=str(date)


    if request.method == 'POST':
        name2 = request.form['name2']
        date2 = request.form['date2']
        date2=str(date2)

    if request.method == 'POST':
        name3 = request.form['name3']
        date3 = request.form['date3']
        date3=str(date3)
        
    data={'Event_Name':[name,name2,name3],'Date':[date,date2,date3]}
    df = pd.DataFrame(data, columns = ['Event_Name', 'Date'])
                             
    print(df)
    df.to_csv('event.csv', index=False)

    # f=request.form['event.csv']
    
    # # with open(f) as file:
    # df=csv.reader(df)
    # for row in df:
    #  data.append(row)
    # return render_template('data.html',data=data)        

    # df = pd.read_csv('event.csv')
    # df.append({'Event Name': name, 'Date': date },ignore_index=True)
   
        
    # return render_template('new.html',df=df.to_csv('event.csv',header=True,index=False))           
    return render_template('new.html', n=name, s=date,n2=name2,s2=date2,n3=name3,s3=date3) 
        
     

    return render_template('index.html')
    return name	
 

if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port=PORT)