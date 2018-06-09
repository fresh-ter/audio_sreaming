import pyaudio
import socket

port = 5000
ip = "127.0.0.1"

frames = 256
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 48000

p = pyaudio.PyAudio()
stream = p.open(
    format=FORMAT,
    channels=CHANNELS,
    rate=RATE,
    output=True,
    frames_per_buffer=frames
)

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((ip, port))

while True:
    data = client_socket.recv(1024)
    stream.write(data, frames)
