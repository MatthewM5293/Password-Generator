import datetime
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
    def __init__(self, phrase='', password_length=8, has_uppercase=True, has_numbers=True, has_special_character=True):
        self.__password = ''
        self.__phrase = phrase
        self.__password_length = password_length
        self.__has_uppercase = has_uppercase
        self._has_number = has_numbers
        self.__has_special_character = has_special_character
        self.__date_created = datetime.datetime.now()

    def get_password(self):
        return self.__password

    def generate_password(self):
        characters_to_use = string.ascii_lowercase
        if self.__has_uppercase:
            characters_to_use += string.ascii_uppercase
        if self.__has_special_character:
            special_characters = "@#$%^&*-_!+=[]{}|\\:'\",.?/`~"
            characters_to_use += special_characters
            pass
        if self._has_number:
            characters_to_use += string.digits
        if self.__phrase != '':
            characters_to_use += self.__phrase
        self.__password = ''.join(random.choices(characters_to_use, k=self.__password_length, ))
        return self.__password
