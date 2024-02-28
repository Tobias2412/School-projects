import PySimpleGUI as sg

layout = [
    [sg.Text('Input temperature:')],
    [sg.InputText(key='-TEMPERATURE-'), sg.Button('Celsius to Fahrenheit'), sg.Button('Fahrenheit to Celsius')],
]

window = sg.Window('Temperature converter', layout)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    temperature = float(values['-TEMPERATURE-'])
    if event == 'Celsius to Fahrenheit':
        result = (temperature * 9/5) + 32
    elif event == 'Fahrenheit to Celsius':
        result = (temperature - 32) * 5/9
    window['-TEMPERATURE-'].update(result)

window.close()
