import random
import string
import PySimpleGUI as sg

# Components:
# Characters, Password
# Then print components


def PassGen():
    password_characters = string.ascii_letters + string.punctuation + string.digits
    password = "".join(random.choice(password_characters) for x in range(random.randint(16, 32)))
    return password


def MainGUI():
    layout = [  [sg.Text("Click 'Generate' to generate password!")],
                (sg.Output(size=(50, 1), key="-OUTPUT-"),),
                [sg.Button("Generate"), sg.Button("Exit")]    ]

    window = sg.Window("Random Password Generator v1.0", layout)

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            break
        elif event == 'Generate':
            window["-OUTPUT-"].update("")
            print(PassGen())
    window.close()
MainGUI()