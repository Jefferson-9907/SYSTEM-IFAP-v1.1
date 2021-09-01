class ParaleloRegistration:
    """
        Esta clase es una clase modelo para obtener valores del formulario de registro del paralelo y
        establecer todos los datos en la tabla de la base de datos backend llamada Course_Window
    """

    def __init__(self, id_paralelo, nombre_cur, nombre_par, dia, hora, f_ini, f_fin, duracion):
        self.__id_paralelo = id_paralelo
        self.__nombre_cur = nombre_cur
        self.__nombre_par = nombre_par
        self.__dia = dia
        self.__hora = hora
        self.__f_ini = f_ini
        self.__f_fin = f_fin
        self.__duracion = duracion

    # ===========================set methods=======================
    def set_id_paralelo(self, id_paralelo):
        self.__id_paralelo = id_paralelo

    def set_nombre_cur(self, nombre_cur):
        self.__nombre_cur = nombre_cur

    def set_nombre_par(self, nombre_par):
        self.__nombre_par = nombre_par

    def set_dia(self, dia):
        self.__dia = dia

    def set_hora(self, hora):
        self.__hora = hora

    def set_f_ini(self, f_ini):
        self.__f_ini = f_ini

    def set_f_fin(self, f_fin):
        self.__f_fin = f_fin

    def set_duracion(self, duracion):
        self.__dia = duracion

    # =====================get methods========================
    def get_id_paralelo(self):
        return self.__id_paralelo

    def get_nombre_cur(self):
        return self.__nombre_cur

    def get_nombre_par(self):
        return self.__nombre_par

    def get_dia(self):
        return self.__dia

    def get_hora(self):
        return self.__hora

    def get_f_ini(self):
        return self.__f_ini

    def get_f_fin(self):
        return self.__f_fin

    def get_duracion(self):
        return self.__duracion


class GetDatabase:
    def __init__(self, database):
        self.__database = database

    def get_database(self):
        return self.__database
