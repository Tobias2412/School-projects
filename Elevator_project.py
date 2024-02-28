import time
from machine import Pin
import network
import gc
import socket
gc.collect()

ssid = 'ITEK 1st'
password = 'iteke23a'

station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(ssid, password)

while station.isconnected() == False:
  pass

print('Connection successful')
print(station.ifconfig())

pin1 = Pin(0, mode=Pin.OUT)  # Motor pin 1
pin2 = Pin(1, mode=Pin.OUT)  # Motor pin 2

gy53 = Pin(16, Pin.IN)  # Distance sensor pin

# Define elevator levels
levels = {
    'ground_floor': 320,  # example values in mm
    'first_floor': 210,
    'second_floor': 120
}

# Functions to control the motor
def forward():
    pin1.on()
    pin2.off()

def backwards():
    pin1.off()
    pin2.on()

def stop():
    pin1.off()
    pin2.off()

# Function to measure distance
def measure_distance():
    while gy53.value() == True:
        pass
    while gy53.value() == False:
        pass
    startTime = time.ticks_us()
    while gy53.value() == True:
        pass
    endtime = time.ticks_us()
    print((endtime - startTime) / 10)
    return (endtime - startTime) / 10   # distance in mm

# Function to move the elevator to a specified level
def move_to_level(target_level):
    while True:
        current_distance = measure_distance()
        if abs(current_distance - target_level) < 20:  # 20mm margin
            stop()
            break
        elif current_distance < target_level:
            forward()
        else:
            backwards()
        time.sleep(0.3)  # Adjust for finer control

def web_page():
    html = """
            <html>
            <head>
                <meta name="viewport" content="width=device-width, initial-scale=1">
                <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.7.2/css/all.css"
                 integrity="sha384-fnmOCqbTlWIlj8LyTjo7mOUStjsKC4pOpQbqyi7RrhN7udi9RwhKkMHpvLbHG9Sr" crossorigin="anonymous">
                <style>
                    html {
                        font-family: Arial;
                        display: inline-block;
                        margin: 0px auto;
                        text-align: center;
                    }

                    .button {
                        background-color: #4CAF50;
                        border: none;
                        color: white;
                        padding: 16px 40px;
                        text-align: center;
                        text-decoration: none;
                        display: inline-block;
                        font-size: 16px;
                        margin: 4px 2px;
                        cursor: pointer;
                    }
                </style>
            </head>
            <body>
                <h2>Raspberry Pi Pico Elevator Control</h2>
                <p>
                    <a href="/ground_floor"><button class="button">Ground Floor</button></a>
                    <a href="/first_floor"><button class="button">First Floor</button></a>
                    <a href="/second_floor"><button class="button">Second Floor</button></a>
                </p>
            </body>
            </html>
            """
    return html
    pass

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)

while True:
    conn, addr = s.accept()
    request = conn.recv(1024)
    conn.settimeout(None)
    request = str(request)

    if '/ground_floor' in request:
        move_to_level(levels['ground_floor'])
    elif '/first_floor' in request:
        move_to_level(levels['first_floor'])
    elif '/second_floor' in request:
        move_to_level(levels['second_floor'])

    response = web_page()
    conn.send('HTTP/1.1 200 OK\n')
    conn.send('Content-Type: text/html\n')
    conn.send('Connection: close\n\n')
    conn.sendall(response)
    conn.close()