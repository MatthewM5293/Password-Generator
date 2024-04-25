import json


class Database:
    def __init__(self):
        self.__filename = "database.json"
        self.__database = []

    def __read_database_from_file(self):
        try:
            with open(self.__filename, "r") as f:
                __input = f.read()
                self.__database = json.loads(__input)
        except:
            self.__write_to_database([])
        return self.__database

    def __write_to_database(self, record):
        with open(self.__filename, "w") as f:
            f.write(json.dumps(record, indent=4))

    def __append_to_database(self, password):
        self.__database = self.__read_database_from_file()
        self.__database.append(password)
        self.__write_to_database(self.__database)

    def __remove_from_database(self, record):
        # print(f'removed {record[0], record[1], record[2]} from database')
        self.__database.remove(record)
        self.__write_to_database(self.__database)

    def __find_in_database(self, record):
        self.__database = self.__read_database_from_file()
        for element in self.__database:
            if element.lower() == record.lower():
                return element
        return

    def list_database(self):
        self.__database = self.__read_database_from_file()
        if not self.__database:
            print("No data in the database, try adding some!")
            # return empty list
        else:
            print('listing all records in the database:')
            # return database

    # endregion

    def decrypt_database(self, input):
        # parse input with secret key
        decrypted = ''
        return decrypted

    def encrypt_database(self):
        encrypted = ''
        return encrypted
