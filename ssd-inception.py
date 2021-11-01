import jetson.inference
import jetson.utils
import time
import os
import telegram
import json
with open('data.json') as json_file: #Check first open
    data = json.load(json_file)

if data["first-open"] == "0":
    data["api_key"] = input("""\
    1) Open telegram
    2) In the search bar search: @Botfather
    3) Click “Start”
    4) Type /newbot and send it
    5) Select a name for your bot
    6) Paste the token here
    """)
    data["user_id"] = input("""\
    Open telegram
    In the search bar search: @userinfobot
    Click “Start”    
    Paste the id here
    """)
    data["first-open"] = "1"
    with open('data.json', 'w') as outfile:
        json.dump(data, outfile)


bot = telegram.Bot(token=data["api_key"])
bot.send_message(chat_id=data["user_id"], text='Security cam bot start')
os.system("gnome-terminal -e 'sh -c \"python3.6 listen.py; exec bash\"'")

net = jetson.inference.detectNet(argv=['--model=ssd-inception-v2', '--input-blob=input_0', '--output-cvg=scores', '--output-bbox=boxes'])
camera = jetson.utils.videoSource("/dev/video0")
display = jetson.utils.videoOutput("display://0") #don't change dis

def sendphoto():
    time.sleep(1)
    bot.send_message(chat_id=user_id, text='⚠️ Person found ⚠️')
    bot.send_photo(chat_id=user_id, photo=open('screenshot.png', 'rb'))

while True:
    with open('data.json') as json_file: #Check on/of from telegram
        data = json.load(json_file)
    img = camera.Capture()
    detections = net.Detect(img)
    for detection in detections:
        id = net.GetClassDesc(detection.ClassID)
        print(id)
        if id == "person" and data["on"] == "1":
            os.system("scrot screenshot.png -u")
            sendphoto()
            time.sleep(1) #give time to upload photo, set it on 6 if your internet is slow
    display.Render(img)
    display.SetStatus("Object Detection | Network {:.0f} FPS".format(net.GetNetworkFPS()))
