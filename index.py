from flask import Flask,request,Response
from cnxn import cursor,cnxn
from datetime import timedelta
import datetime

now = datetime.datetime.now()

app = Flask(__name__)

@app.route("/")
def home():
    return "Webservice Insert Call Information to Database"

@app.route("/test")
def test():
    r = "<?xml version=\"1.0\" encoding=\"utf-8\"?>\n<RESULT>\n<RESULT_STATUS>TRUE</RESULT_STATUS>\n</RESULT>"
    return Response(r, mimetype='text/xml')

@app.route('/insert')
def insert():
    time = str(datetime.datetime.now())
    timeadded = str(datetime.datetime.now() + timedelta(minutes=2))

    SessionID = request.args.get('SessionID')
    IVRMenu = request.args.get('IVRMenu')
    CSQ = request.args.get('CSQ')
    CustomerNumber = request.args.get('CustomerNumber')
    CallBackNumber = request.args.get('CallBackNumber')
    CallType = request.args.get('CallType')
    OriginalStampDateTime = time[:-3]
    StampDateTime = timeadded[:-3]
    
    cursor.execute("INSERT INTO dbo.CallBack_Abandon_Emergency(SessionID, IVRMenu, CSQ, CustomerNumber, CallBackNumber, CallType, Original_StampDateTime, StampDateTime) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", 
        SessionID, 
        IVRMenu,
        CSQ,
        CustomerNumber,
        CallBackNumber,
        CallType,
        OriginalStampDateTime,
        StampDateTime )
    cnxn.commit()

    r = "<?xml version=\"1.0\" encoding=\"utf-8\"?>\n<RESULT>\n<RESULT_STATUS>TRUE</RESULT_STATUS>\n</RESULT>"
    return Response(r, mimetype='text/xml')

@app.route('/update')
def update():
    SessionID = request.args.get('SessionID')
    time = str(datetime.datetime.now())
    StampDateTime = time[:-3]

    cursor.execute("UPDATE dbo.CallBack_Abandon_Emergency SET CallType = 'Handle', StampDateTime = ? WHERE SessionID = ?;", StampDateTime, SessionID )
    cnxn.commit()

    r = "<?xml version=\"1.0\" encoding=\"utf-8\"?>\n<RESULT>\n<RESULT_STATUS>TRUE</RESULT_STATUS>\n</RESULT>"
    return Response(r, mimetype='text/xml')

if __name__ == '__main__':
  app.debug = True
  app.run(host='0.0.0.0')
  #app.run(host='0.0.0.0', port=8000)
