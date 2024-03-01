# list audio devices
# user choses the preferred audio input
# initiate audio input streaming

# set a silence threshold for phrase framing
# queue the audio clip
# process the clip through the model

import sounddevice as sd
import time

devices = sd.query_devices()
print(devices)

# def audio_callback(indata, frames, time, status):
#     if status:
#         print(time, status)

# try:
#   selected_device_id = int(input("Enter the device ID you'd like to use: "))
#   if selected_device_id < 0 or selected_device_id >= len(devices):
#     ValueError("Invalid device selection!")
#   selected_device = devices[selected_device_id]
#   print("Selected device: " + selected_device['name'])

#   stream = sd.InputStream(
#         device=selected_device, channels=2, callback=audio_callback)  
# except Exception as ex:
#   print(ex)
