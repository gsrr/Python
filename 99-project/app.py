from flask import Flask,redirect,render_template,request
import requests

app = Flask(__name__)

@app.route('/')
def index():
    dom = requests.get(
        "https://opendata.cwb.gov.tw/api/v1/rest/datastore/O-A0003-001?Authorization=CWB-5550E562-D27B-4DDE-AB03-D1D88DA02F01&format=JSON"
    ).json()

    location = dom['records']['location'][11]['parameter'][0]['parameterValue']
    temp = dom['records']['location'][11]['weatherElement'][3]['elementValue']
    Name = dom['records']['location'][11]['weatherElement'][3]['elementName']
    print(location + temp +":"+Name)
    return render_template('index.html',location=location,temp=temp,Name=Name)

@app.route('/user/<name>')
def user(name):
    return '<h1>Hello,{}</h1>'.format(name)

if __name__ == '__main__':
    #app.run(host="0.0.0.0", port=5000, ssl_context=('./cert/CA.pem','./cert/CA.key'))
    app.run(host="0.0.0.0", port=5000)
