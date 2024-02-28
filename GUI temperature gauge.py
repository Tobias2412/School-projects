import PySimpleGUI as sg

layout = [
    [sg.Text('Input temperature in Celsius:')],
    [sg.InputText(key='-CELSIUS-')],
    [sg.Button('Convert')]
]

window = sg.Window('Celsius to Fahrenheit', layout)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    if event == 'Convert':
        celsius = float(values['-CELSIUS-'])
        fahrenheit = (celsius * 9/5) + 32
        sg.popup(f'The temperature in Fahrenheit is: {fahrenheit:.2f}')

window.close()
