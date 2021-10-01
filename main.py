import jetson.inference
import jetson.utils
import time
import os
import telegram

api_key = 'bot_api_key_here'
user_id = 'user_id_here'
bot = telegram.Bot(token=api_key)
bot.send_message(chat_id=user_id, text='Jetson Security Camera started')

net = jetson.inference.detectNet(argv=['--model=model/ssd-mobilenet.onnx', '--labels=model/labels.txt', '--input-blob=input_0', '--output-cvg=scores', '--output-bbox=boxes'])
camera = jetson.utils.videoSource("/dev/video0")
display = jetson.utils.videoOutput("display://0") #don't change dis

def sendphoto():
    time.sleep(1)
    bot.send_message(chat_id=user_id, text='⚠️ Person found ⚠️')
    bot.send_photo(chat_id=user_id, photo=open('screenshot.png', 'rb'))

while True:
    img = camera.Capture()
    detections = net.Detect(img)
    for detection in detections:
        id = net.GetClassDesc(detection.ClassID)
        print(id)
        if id == "Person":
            os.system("scrot screenshot.png -u")
            sendphoto()
            time.sleep(1) #give time to upload photo, set it on 6 if your internet is slow
    display.Render(img)
    display.SetStatus("Object Detection | Network {:.0f} FPS".format(net.GetNetworkFPS()))
