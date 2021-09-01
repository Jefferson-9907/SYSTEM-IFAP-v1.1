class ConnectDatabase:
    """this is the model class for ConnectDatabase class from module connect_database, it connects frontend and
    backend """
    def __init__(self, host, username, password):
        self.__host = host
        self.__username = username
        self.__password = password

    def get_host(self):
        return self.__host

    def get_username(self):
        return self.__username

    def get_password(self):
        return self.__password


class CreateDatabase:
    def __init__(self, database):
        self.__database = database

    def get_database(self):
        return self.__database
