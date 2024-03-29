from flask import Flask,redirect,url_for,render_template,request
import flask
from flask_cors import CORS,cross_origin
# import pymongo as pmb
import datetime
import os
app=Flask(__name__)

# client = pmb.MongoClient('mongodb+srv://Saiprasad:Srihari@cluster0.kkyyt.mongodb.net/WebIp?retryWrites=true&w=majority')

# db = client['mywebip']


@app.route('/',methods=['GET','POST'])
@cross_origin()
def home():
#     ip_address = str(request.remote_addr)
#     print(ip_address)
#     db.ipaddr.insert_one({"timeStamp": datetime.datetime.now(),"ip_Address":ip_address})
    return render_template('index.html')

@app.route('/static/Resume.pdf',methods=['GET','POST'])
@cross_origin()
def downnload():
    return flask.send_from_directory(directory="static",    filename='Resume.pdf')

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    #app.run()
    app.run(host='0.0.0.0', port=port)
    # 
