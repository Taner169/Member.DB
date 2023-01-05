import PySimpleGUI as sg
import interface
import Information
import validation



layout = [[sg.Text("First Name:"), sg.Push(), sg.Input(key='-FIRSTNAME-', do_not_clear=True, size=(40, 3))],
          [sg.Text("Last Name:"), sg.Push(), sg.Input(key='-LASTNAME-', do_not_clear=True, size=(40, 3))],
          [sg.Text("Street Address:"), sg.Push(), sg.Input(key='-STREETADDRESS-', do_not_clear=True, size=(40, 3))],
          [sg.Text("ZIP Code:"), sg.Push(),  sg.Input(key='-ZIPCODE-', do_not_clear=True, size=(40, 3))],
          [sg.Text("Mail:"), sg.Push(), sg.Input(key='-MAIL-', do_not_clear=True, size=(40, 3))],
          [sg.Text("Payed Fee:"), sg.Push(),  sg.Input(key='-PAYEDFEE-', do_not_clear=True, size=(40, 3))],
          [sg.Button('Submit Member Information',expand_x=True), sg.Button('Show Table',expand_x=True), sg.Exit()]]

window = sg.Window("Submit Member Information", layout)

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    elif event == 'Submit Member Information':
        validation_result = validation.validate(values)
        if validation_result["is_valid"]:
            interface.insert_member(values['-FIRSTNAME-'], values['-LASTNAME-'],
                                     values['-STREETADDRESS-'], values['-ZIPCODE-'], values['-MAIL-'], values['-PAYEDFEE-'])
            sg.popup("Member Information submitted!")

        else:
            error_message = validation.generate_error_message(validation_result["values_invalid"])
            sg.popup(error_message)
    elif event == 'Show Table':
        Information.create()
