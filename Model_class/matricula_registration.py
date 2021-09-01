class MatriculaRegistration:
    """
        Esta clase es una clase modelo para obtener valores del formulario de registro del curso y
        establecer todos los datos en la tabla de la base de datos backend llamada Course_Window
    """

    def __init__(self, id_matricula, estudiante, paralelo, asesor):
        self.__id_matricula = id_matricula
        self.__id_estudiante = estudiante
        self.__paralelo = paralelo
        self.__asesor = asesor

    # ===========================set methods=======================
    def set_id_matricula(self, id_matricula):
        self.__id_matricula = id_matricula

    def set_estudiante(self, estudiante):
        self.__estudiante = estudiante

    def set_paralelo(self, paralelo):
        self.__paralelo = paralelo

    def set_asesor(self, asesor):
        self.__asesor = asesor

    # =====================get methods========================
    def get_id_matricula(self):
        return self.__id_matricula

    def get_estudiante(self):
        return self.__estudiante

    def get_paralelo(self):
        return self.__paralelo

    def get_asesor(self):
        return self.__asesor


class GetDatabase:
    def __init__(self, database):
        self.__database = database

    def get_database(self):
        return self.__database
