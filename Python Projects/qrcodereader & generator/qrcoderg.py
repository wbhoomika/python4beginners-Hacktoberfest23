import sys,qrcode
from qrtools import QR
from easygui.boxes.derived_boxes import msgbox,  ccbox, enterbox, multenterbox
from easygui.boxes.base_boxes import buttonbox, fileopenbox
while 1:    
    msg = "QR CODE Read And Generator."
    title = "QR Code"
    choices = ["Read","Generate"]
    choice = buttonbox(msg, title, choices)
    if str(choice) == "Read":
        '''QR Reader code will go here...'''
        #print "qr code read"
        file = fileopenbox()
        #print file1 -- displays path of file
        dec = QR(filename=file)
        if dec.decode():
            msgbox(dec.data, "Your decoded data",)
        else:
            print dec.error
        msg = "Cancel to exit"
        title = "Want to Continue?"
        if ccbox(msg,title):
            pass
        else:
            sys.exit(0)
    else:
        '''QR Code Generator code will go here....'''

        #ddata = enterbox(msg="Enter data to decode:",title="Data Decode")
        fld = ["Data to decode","Image name with extension"]
        fields = []
        fields = multenterbox("Enter data to decode:","DAta Decode",fld)
        img = qrcode.make(fields[0])
        img.save(fields[1])
        msg = "Cancel to exit"
        title = "Want to Continue?"
        if ccbox(msg,title):
            pass
        else:
            sys.exit(0)
