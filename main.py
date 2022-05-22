from requests import request
# from sockettest import app,socketio
from math2 import app

if __name__=="__main__":
   # app.run(host='0.0.0.0',port=3000,debug=True)
   app.run(host='127.0.0.1', port=5000 ,debug=True)


# if __name__ == "__main__":
#     socketio.run(app,host='0.0.0.0',port=3000,debug=True)