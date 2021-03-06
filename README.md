# Jetson Security Camera
![](https://github.com/epicmario7133/jetson-security-camera/raw/main/header.jpg)
Jetson Security Camera is a program to make your security camera "intelligent", using [pytorch](https://pytorch.org/ "pytorch") and a model trained to recognize people during the day and night and then notify you via telegram.
# Download and configuration
Install jetson-inference
```
sudo apt-get update
sudo apt-get install git cmake libpython3-dev python3-numpy nano scrot python3-pip
git clone --recursive https://github.com/dusty-nv/jetson-inference
cd jetson-inference
mkdir build
cd build
cmake ../
make -j$(nproc)
ATTENTION YOU WILL GET WRITTEN ASKING FOR THE MODELS TO DOWNLOAD, YOU MUST CHOOSE ALL MODELS OBJECT DETECTION
sudo make install
sudo ldconfig
```

Go back to the root directory and do this command:

```
pip3 install python-telegram-bot --upgrade
git clone https://github.com/epicmario7133/jetson-security-camera.git
mkdir model
cd model
wget https://epicmario71.com/model/ssd-mobilenet.onnx
wget https://epicmario71.com/model/labels.txt
cd ..
```

Now we need to define the video input by editing line 35, by default the usb camera is used, here you have a scheme of which input you can use



|                  | Protocol     | Resource URI              | Notes                                                    |
|------------------|--------------|---------------------------|----------------------------------------------------------|
| [MIPI CSI camera] | `csi://`     | `csi://0`                 | CSI camera 0 (substitute other camera numbers for `0`)                    |
| [V4L2 camera]   | `v4l2://`    | `v4l2:///dev/video0`      | V4L2 device 0 (substitute other camera numbers for `0`)                            |
| [RTP stream]       | `rtp://`     | `rtp://@:1234`            | localhost, port 1234 (requires additional configuration) |
| [RTSP stream]    | `rtsp://`    | `rtsp://<remote-ip>:1234` | Replace `<remote-ip>` with remote host's IP or hostname  |
| [Video file]       | `file://`    | `file://my_video.mp4`     | Supports loading MP4, MKV, AVI, FLV (see codecs below)   |
| [Image file]     | `file://`    | `file://my_image.jpg`     | Supports loading JPG, PNG, TGA, BMP, GIF, ect.           |
| [Image sequence]  | `file://`    | `file://my_directory/`    | Searches for images in alphanumeric order                |

[scheme source](https://github.com/dusty-nv/jetson-inference/blob/master/docs/aux-streaming.md "scheme source")

Then run the program like this:
```
python3.6 main.py
```
Now ask you to generate a telegram bot the instructions are already inside the program


To deactivate or reactivate the function that sends the warning on the telegram just do this command on the telegram:

To turn off:
```
/off
```
To turn on:
```
/on
```


# Model information:
40000 images of people during the day

20000 images of people at night (most in black and white)

# Pros and cons:
Pros:
- Can send photos if a person is inside your home
- It can find people even at night

Cons:
- at night the person must be in the center of the camera to be found

# Demo video:
[![youtube video](https://i.ibb.co/ssQVpzb/mq2.jpg)](https://www.youtube.com/watch?v=5b4fPcDmFr4)

# Difference between ssd inception model and main model

[![youtube video](https://i.ibb.co/XjMmHcP/mq1.jpg)](https://www.youtube.com/watch?v=M06uGCzwmfI)

Here we can see the difference between the ssd inception model and the main model (the one found in main.py), as we can see the ssd inception model makes more mistakes to find people in the video but it recognizes people almost imediately, while the main model takes longer to find people but makes no mistake in finding them

# Difference between the paid model and the free model

[![youtube video](https://i.ibb.co/QJfKYxq/mq3.jpg)](https://www.youtube.com/watch?v=gqNN1YED2zk)

Here we can see the difference of the free model and the paid model, the free model was made with 60000 images and one epoch, while the paid one is made with 150000 and 5 epochs (it will be improved every month)
