import PySimpleGUI as SG

from Password import Password


class UI:
    def __init__(self):
        self.lst_passwords = []
        self.layout = [
            [SG.Text('Welcome to Password Generator!')],
            [SG.Combo(values=[8, 9, 10, 11, 12, 13, 14, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25], readonly=True,
                      size=17, key='-password-length-', default_value=25, enable_events=True),
             SG.Radio('Use special characters', key='-use-special-characters-', default=True, group_id=1),
             SG.Radio('Use uppercase characters', key='-use-uppercase-characters-', default=True, group_id=2),
             SG.Radio('Use numbers', key='-use-number-characters-', default=True, group_id=3),
             ],
            [SG.Button('Generate Password', key='-generate-password-')],
            [SG.LBox(values=self.lst_passwords, size=(100, 20), key='-PASSWORDS-', visible=False)],
            [SG.Button('Show All Passwords', key='-show-passwords-')]
        ]
        self.window = SG.Window('Password Generator', self.layout)

    def start_ui(self):
        password = Password()
        while True:
            event, values = self.window.read()
            if event == SG.WIN_CLOSED:
                break
            elif event == '-generate-password-':
                password = Password(values['-passwod-length-'], values['-use-uppercase-characters-'],
                                    values['-use-number-characters-'], values['-use-special-characters-'])
                password.generate_password()
            elif event == '-password-length-':
                print(values['-password-length-'])  # gets int from combo box
            elif event == '-show-passwords-':
                self.update_ui()
        self.window.close()

    def update_listbox(self):
        # arr_image = []
        # call list function in DB
        self.window['-PASSWORDS-'].update([])
        self.window.refresh()

    def update_ui(self):
        event, values = self.window.read()
        if values['-PASSWORDS-'] and (values['-PASSWORDS-'] != '' or values['-PASSWORDS-'] != []):
            # show LBox in UI
            self.window['-PASSWORDS-'].update(visible=True)
            self.window.refresh()
        else:
            # hide LBox from UI
            self.window['-PASSWORDS-'].update(visible=False)
            self.window.refresh()


if __name__ == '__main__':
    ui = UI()
    ui.start_ui()
