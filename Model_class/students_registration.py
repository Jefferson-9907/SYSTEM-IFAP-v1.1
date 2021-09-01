class StudentsRegistration:
    """
        Esta clase es una clase modelo para obtener valores del formulario de registro del estudiante y
        establecer todos los datos en la tabla de la base de datos backend llamada estudiantes
    """

    def __init__(self, cedula_al, nombres_al, apellidos_al, edad_al, direccion_al, correo_al, celular_al, telefono_al,
                 representante_al, n_c_representante_al, observacion_al):
        self.__cedula_al = cedula_al
        self.__nombres_al = nombres_al
        self.__apellidos_al = apellidos_al
        self.__edad_al = edad_al
        self.__direccion_al = direccion_al
        self.__correo_al = correo_al
        self.__celular_al = celular_al
        self.__telefono_al = telefono_al
        self.__representante_al = representante_al
        self.__n_c_representante_al = n_c_representante_al
        self.__observacion_al = observacion_al

    # ===========================set methods=======================

    def set_cedula_al(self, cedula_al):
        self.__cedula_al = cedula_al

    def set_nombres_al(self, nombres_al):
        self.__nombres_al = nombres_al

    def set_apellidos_al(self, apellidos_al):
        self.__apellidos_al = apellidos_al

    def set_edad_al(self, edad_al):
        self.__edad_al = edad_al

    def set_direccion_al(self, direccion_al):
        self.__direccion_al = direccion_al

    def set_correo_al(self, correo_al):
        self.__correo_al = correo_al

    def set_celular_al(self, celular_al):
        self.__celular_al = celular_al

    def set_telefono_al(self, telefono_al):
        self.__telefono_al = telefono_al

    def set_representante_al(self, representante_al):
        self.__representante_al = representante_al

    def set_n_c_representante_al(self, n_c_representante_al):
        self.__n_c_representante_al = n_c_representante_al

    def set_observacion_al(self, observacion_al):
        self.__observacion_al = observacion_al

    # =====================get methods========================

    def get_cedula_al(self):
        return self.__cedula_al

    def get_nombres_al(self):
        return self.__nombres_al

    def get_apellidos_al(self):
        return self.__apellidos_al

    def get_edad_al(self):
        return self.__edad_al

    def get_direccion_al(self):
        return self.__direccion_al

    def get_correo_al(self):
        return self.__correo_al

    def get_celular_al(self):
        return self.__celular_al

    def get_telefono_al(self):
        return self.__telefono_al

    def get_representante_al(self):
        return self.__representante_al

    def get_n_c_representante_al(self):
        return self.__n_c_representante_al

    def get_observacion_al(self):
        return self.__observacion_al


class GetDatabase:
    def __init__(self, database):
        self.__database = database

    def get_database(self):
        return self.__database

