import PySimpleGUI as sg
import interface
import sqlite3

def get_member_records():
    member_records = interface.retrieve_members()
    return member_records




def create():
    member_records_array = get_member_records()
    headings = ['First Name', 'Last Name', 'Street Address', 'Zip Code', 'Mail', 'Payed Fee']

    member_information_window_layout = [
        [sg.Table(values=member_records_array, headings=headings, max_col_width=35,
                  auto_size_columns=True,
                  display_row_numbers=True,
                  justification='right',
                  num_rows=10,
                  key='-TABLE-',
                  row_height=35,
                  tooltip='Reservations Table')],
        [sg.Button('Delete',expand_x=True), sg.Button('Search',expand_x=True)]
    ]

    member_information_window = sg.Window("Member Information Window",
                                           member_information_window_layout, modal=True)


    while True:
        event, values = member_information_window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        elif event == 'Delete':
            interface.delete_member_by_name(first_name=True)
