import PySimpleGUI as sg

sg.theme("DarkAmber")

text_el1 = sg.Text("This is a text element")
input_1 = sg.Input(key="-IN-")
btn_ok = sg.Button("Ok")
btn_exit = sg.Button("Exit")
layout = [[text_el1], [input_1], [ btn_ok, btn_exit]]

window = sg.Window("Title", layout)

while True:
    event, values = window.read()
    print(event, values)
    if event in (sg.WIN_CLOSED, "Exit"):
        break
    

window.close()

