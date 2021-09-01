import mariadb


def solo_numero(char):
    return char in '1234567890.'


def conexion_consulta(consulta, parametros=()):
    conexion = mariadb.connect(host="localhost", user="root", passwd="", database="system_bd_ifap")
    try:  # Captura la excepcion en caso de que algo falle
        cursor = conexion.cursor()
        conexion_consulta(consulta, parametros)
        resultado = cursor.execute(consulta, parametros)  # Establece la consulta sql a realizar y sus parametros
        conexion.commit()

        return resultado

    except Exception as e:
        print(e)
        conexion.close()
        return False
