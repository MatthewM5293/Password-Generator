import random
import string

'''
Characters Allowed
    A-Z
    a-z
    0-9
    
Characters Not Allowed
    Unicode characters
    Spaces
    Strong passwords only: Cannot contain a dot character (.) immediately preceding the @ symbol

Password Restrictions
    Eight (8) characters is the minimum and sixteen (16) characters is the maximum
    Strong passwords only: Three of the following are required:
    Lowercase characters
    Uppercase characters
    Numbers (0-9)
    Symbols (see the symbols listed in Characters Allowed above)
'''


class Password:
    def __init__(self, password_length=8, has_uppercase=True, has_numbers=True, has_special_character=True):
        self.__password = ''
        self.__nickname = ''
        self.__password_length = password_length
        self.__has_uppercase = has_uppercase
        self._has_number = has_numbers
        self.__has_special_character = has_special_character

    def set_password(self, password):
        self.__password = password

    def set_nickname(self, nickname):
        self.__nickname = nickname

    def set_has_special_character(self, has_special_character):
        self.__has_special_character = has_special_character

    def set_has_uppercase(self, has_uppercase):
        self.__has_uppercase = has_uppercase

    def set_has_number(self, has_number):
        self.__has_uppercase = has_number

    def generate_password(self):
        if self.__has_uppercase:
            # generate password as normal using __password_length variable to make it dynamic
            self.__password = ''.join(random.choices(string.ascii_lowercase + string.digits + string.ascii_uppercase,
                                                     k=self.__password_length))
            print(self.__password)
            # make a random char in it upper case (future: will make a certain amount of chars uppercase)
            # get random char in self.__password, make it uppercase
            self.__password = ''.join(random.choices(string.ascii_lowercase + string.digits + string.ascii_uppercase,
                                                     k=self.__password_length))
            # check if has number, else replace a lowercase char with a special char
            pass
        if self.__has_special_character:
            # check if has special char, else replace a lowercase char with a special char (@ # $ % ^ & * - _ ! + = [] {} | \ : ’ , . ? / ` ~ ” () ;)
            pass
        if self._has_number:
            self.__password = ''.join(random.choices(string.ascii_lowercase + string.digits + string.ascii_uppercase,
                                                     k=self.__password_length))

    def verify_custom_input(self, input_string):
        # verify input with regex to make sure it complies with specifications above
        pass
