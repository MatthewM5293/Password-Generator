import PySimpleGUI as sg

from Password import Password


class UI:
    def __init__(self):
        self.__lst_passwords = []
        self.__layout = [
            [sg.Text('Welcome to Password Generator!')],
            [sg.Checkbox('Enter special characters (Not all may be used)', key='-special-phrase-', enable_events=True),
             sg.Multiline(key='-custom-chars-', size=(28, 1), disabled=False, default_text='',
                          no_scrollbar=True, border_width=0, visible=False, write_only=True, enable_events=True),
             sg.Text('0/20', key='-char-count-', visible=False)],
            [sg.Text('Special characters must be 5 characters less than Password length!', key='-special-phrase-check-',
                     font=('Terminal', 10), text_color='red', visible=False)],
            [sg.Text('Special characters cannot have spaces!', key='-special-phrase-check2-',
                     font=('Terminal', 10), text_color='red', visible=False)],
            [sg.Text('Select password length: '),
             sg.Combo(values=[8, 9, 10, 11, 12, 13, 14, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25], readonly=True,
                      size=10, key='-password-length-', default_value=25, enable_events=True,
                      tooltip='Select length of password'),
             sg.Checkbox(text='Use special characters', key='-use-special-characters-', enable_events=True),
             sg.Checkbox(text='Use uppercase characters', key='-use-uppercase-characters-', enable_events=True),
             sg.Checkbox(text='Use numbers', key='-use-number-characters-', enable_events=True)],

            [sg.Button('Generate Password', key='-generate-password-')],
            [sg.LBox(values=self.__lst_passwords, size=(100, 20), key='-PASSWORDS-', visible=False)],
            [sg.Text(text='Hello mario', key='-output-password-', visible=False)],
            [sg.Button('Show All Passwords', key='-show-passwords-', visible=False)]
        ]
        self.__window = sg.Window('Password Generator', self.__layout, default_element_size=(40, 20),
                                  icon='password.ico', location=(600, 500), element_justification='center')

    def start_ui(self):
        while True:
            event, values = self.__window.read()
            if event == sg.WIN_CLOSED:
                break

            elif event == '-generate-password-':
                password = Password(self.__window['-custom-chars-'].get().rstrip(), values['-password-length-'],
                                    values['-use-uppercase-characters-'],
                                    values['-use-number-characters-'], values['-use-special-characters-'])
                password.generate_password()
                self.__window['-output-password-'].update(value=f'Password Generated: {password.get_password()}',
                                                          visible=True)

            elif event == '-password-length-':
                self.update_char_count(current_length=len(self.__window['-custom-chars-'].get()),
                                       max_length=values['-password-length-'])

            elif event == '-custom-chars-':
                phrase = self.__window['-custom-chars-'].get()
                if len(phrase) > values['-password-length-'] - 5:
                    phrase = phrase[:-1]
                    self.__window['-custom-chars-'].update(phrase)
                    self.__window['-special-phrase-check-'].update(visible=True)
                else:
                    self.__window['-special-phrase-check-'].update(visible=False)
                    if " " in phrase:
                        phrase = phrase[:-2]
                        self.__window['-custom-chars-'].update(phrase)
                        self.__window['-special-phrase-check2-'].update(visible=True)
                    else:
                        self.__window['-special-phrase-check2-'].update(visible=False)

                self.update_char_count(current_length=len(phrase), max_length=values['-password-length-'])

            elif event == '-special-phrase-':
                temp = values['-special-phrase-']
                if temp:
                    # make text field visible for the phrase they want to add
                    self.__window['-custom-chars-'].update(visible=True)
                    self.__window['-char-count-'].update(visible=True)
                else:
                    # hide text field form UI
                    self.__window['-custom-chars-'].update(visible=False)
                    self.__window['-char-count-'].update(visible=False)

            elif event == '-use-special-characters-':
                temp = values['-use-special-characters-']
                self.update_checkbox('-use-special-characters-', temp)

            elif event == '-use-uppercase-characters-':
                temp = values['-use-uppercase-characters-']
                self.update_checkbox('-use-uppercase-characters-', temp)

            elif event == '-use-number-characters-':
                temp = values['-use-number-characters-']
                self.update_checkbox('-use-number-characters-', temp)

            elif event == '-show-passwords-':
                if values['-PASSWORDS-']:
                    self.update_listbox()
                else:
                    self.__window['-PASSWORDS-'].update(visible=False)
        self.__window.close()

    # def update_listbox(self):
    #     # arr_image = []
    #     # call list function in DB
    #     self.window['-PASSWORDS-'].update(visible=True)
    #     self.window.refresh()

    def update_char_count(self, current_length, max_length):
        self.__window['-char-count-'].update(f'{current_length}/{max_length - 5}')
        # self.__window['-custom-chars-'].update(size=(max_length - 5, 1))

    def update_checkbox(self, key, val):
        self.__window[key].update(value=val)
        # self.window.refresh()
