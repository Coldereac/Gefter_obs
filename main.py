import time
import datetime
import subprocess
import webbrowser
from obswebsocket import obsws, requests

start_time = "17:56"
stop_time = "17:57"
zoom_url = "https://us04web.zoom.us/j/4210814329?pwd=RmZtYWFMUUxENWtKUmZWQm9lV1Jodz09"
ws = obsws("localhost", 4444, "248163")
ws.connect()

def stop_recording():
    ws.call(requests.StopRecording())
    subprocess.run("taskkill /IM Zoom.exe /F")

while True:
    now = datetime.datetime.now().strftime("%H:%M")
    if now == start_time:
        webbrowser.open(zoom_url)
        time.sleep(5)
        ws.call(requests.StartRecording())
        print("Запись началась!")
        break
    time.sleep(10)  # Проверять каждые 10 секунд

while True:
    now = datetime.datetime.now().strftime("%H:%M")
    if now == stop_time:
        # Остановка записи
        stop_recording()
        print("Запись завершена!")
        break
    time.sleep(10)  # Проверять каждые 30 секунд
