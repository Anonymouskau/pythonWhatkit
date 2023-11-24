import pywhatkit as kit

from flask_cors import CORS
from datetime import datetime

current_time = datetime.now()

from flask import Flask,request,Response,jsonify

app = Flask(__name__)
CORS(app)  # 
@app.route('/',methods=["GET"])  # Defines a route for the root URL
def hello():
    return 'Server Healthy!'

@app.route('/whatkit',methods=["POST"])  # Defines a route for '/about' URL
def about():
     
     message=request.json["message"]
     
     phone_number=request.json["phone_number"]

     hour=request.json["hours"]                 

     minitue=request.json["miniutes"]  
     
     print(type(hour),type(minitue))
     print(hour,minitue)
     
     if minitue==60 or minitue==59: 

        kit.sendwhatmsg(phone_number,message,hour,2,wait_time=10) 
     else :
         kit.sendwhatmsg(phone_number,message,hour,(minitue+2),wait_time=10)

     return app.response_class(response='sent message',status=200)

if __name__ == '__main__':
    app.run(debug=True,port=8000)

