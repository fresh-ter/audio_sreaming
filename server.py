import pyaudio
import socket
import random

frames = 256

device_info = {}
useloopback = False

p = pyaudio.PyAudio()

try:
    default_device_index = p.get_default_input_device_info()
except IOError:
    default_device_index = -1

print("Available devices:\n")
for i in range(0, p.get_device_count()):
    info = p.get_device_info_by_index(i)
    print(str(info["index"]) + ": \t %s \n \t %s \n" % (info["name"], p.get_host_api_info_by_index(info["hostApi"])["name"]))

    if default_device_index == -1:
        default_device_index = info["index"]

if default_device_index == -1:
    print("No device available. Quitting.")
    exit()

device_id = int(input("Choose device: ")) or default_device_index

try:
    device_info = p.get_device_info_by_index(device_id)
except IOError:
    device_info = p.get_device_info_by_index(default_device_index)
    print("Selection not available, using default.")


is_input = device_info["maxInputChannels"] > 0
is_wasapi = (p.get_host_api_info_by_index(device_info["hostApi"])["name"]).find("WASAPI") != -1
if is_input:
    print("Selection is input using standard mode.\n")
else:
    if is_wasapi:
        useloopback = True
        print("Selection is output. Using loopback mode.\n")
    else:
        print("Selection is input and does not support loopback mode. Quitting.\n")
        exit()


channelcount = device_info["maxInputChannels"] if (device_info["maxOutputChannels"] < device_info["maxInputChannels"])\
    else device_info["maxOutputChannels"]

stream = p.open(
    format=pyaudio.paInt16,
    channels=channelcount,
    rate=int(device_info["defaultSampleRate"]),
    input=True,
    frames_per_buffer=frames,
    input_device_index=device_info["index"],
    as_loopback=useloopback
)
print("Channels:", channelcount)
print("Bitrate:", int(device_info["defaultSampleRate"]))


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('192.168.0.103', 5000))
server_socket.listen(5)
client_socket, address = server_socket.accept()

print("Start listening...")
while True:
    try:
        client_socket.send(stream.read(frames))
    except IOError as e:
        if e == pyaudio.paInputOverflowed:
            print(e)
