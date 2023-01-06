import PySimpleGUI as sg
import interface
import sqlite3
def get_member_records():
    member_records = interface.retrieve_members()
    return member_records

class Search_Delete:
    def success_window(type_of_success: str):  #layout for success

        layout = [[sg.Text(f"Successfully {type_of_success} member!")],
                  [sg.Push(), sg.Button("Close", key="-Close-"), sg.Push()]]

        window = sg.Window("Success!", layout, modal=True, )

        while True:
            event, values = window.read()
            if event == "-Close-":
                window.close()
                break
def Second_Window():  # Shows tabell for members
    conn = sqlite3.connect("member_information.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM member_information")
    rows = cursor.fetchall()

    layout = [[sg.Text("Enter a member for search")], [sg.Button("SEARCH", key="-SEARCH-",expand_x=True)],
              [sg.InputText(default_text=" ", key='-SEARCH_MEMBER-', size=(30, 1),expand_x=True)],
              [sg.Text("")],
              [sg.Push(),
               sg.Table(values=rows,
                        headings=["ID", "First Name", "Last Name", "Address", "Zip Code",
                                  "Mail", "Payed Fee"],
                        auto_size_columns=True,
                        justification="center",
                        row_height=25,
                        key='-TABLE-',
                        enable_events=True,
                        alternating_row_color='IndianRed4'),

               sg.Push()],
              [sg.Text("Enter a Member ID to delete")],
              [sg.Text("Click 2 time to delete in first action")],
              [sg.Button("DELETE", key="-DELETE-",expand_x=True)],
              [sg.Input("", key="-DELETE_MEMBER-",expand_x=True)]]

    window = sg.Window("Members Table", layout, modal=True)
    window.read()

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
#search and Delete function
        if event == '-SEARCH-':
            search_term = values['-SEARCH_MEMBER-']
            cursor.execute("SELECT * FROM member_information WHERE id LIKE ?"
                           "OR First_Name LIKE ? "
                           "OR Last_Name LIKE ?",
                           ('%' + search_term + '%', '%' + search_term + '%',
                            '%' + search_term + '%'))
            rows = cursor.fetchall()
            window['-TABLE-'].Update(values=rows)

        if event == "-DELETE-":
            member = values["-DELETE_MEMBER-"]
            cursor.execute("DELETE from member_information WHERE id = ?", (member,))
            rows_deleted = cursor.rowcount
            if rows_deleted > 0:
                cursor.execute("SELECT * FROM member_information")
                rows = cursor.fetchall()
                window['-TABLE-'].Update(values=rows)
                Search_Delete.success_window("deleted")
            else:
                print("No rows were deleted")

