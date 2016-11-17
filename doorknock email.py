import pyaudio,audioop
import sys
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = sys.argv[1]*60
#smtp settings
import smtplib
#Object
p = pyaudio.PyAudio()
stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)

frames = []

for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    if True:
		reading=audioop.rms(data, 2)
		frames.append(reading)
maxrms=max(frames)
#found out the average disturbance in my room is 20,took a buffer of 1000
if maxrms>5000:
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.ehlo()
	server.starttls()
	server.login("username", "password")
	#Send the mail
	msg = "someone knocked" 
	server.sendmail("from@gmail.com", "to@xyz.com", msg)

		
