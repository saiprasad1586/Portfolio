from flask import Flask,redirect,url_for,render_template,request
from flask_cors import CORS,cross_origin
app=Flask(__name__)


@app.route('/',methods=['GET','POST'])
@cross_origin()
def home():
    return render_template('index.html')

if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD

    app.run(debug=True)