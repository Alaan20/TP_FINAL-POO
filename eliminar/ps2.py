import psycopg2

# Conecta a la base de datos PostgreSQL
def conectar_base_de_datos():
    try:
        connection = psycopg2.connect(
            user="postgres",
            password="teclas",
            host="tpphost.duckdns.org",
            port="5432",
            database="[autosoft]"
        )
        return connection
    except (Exception, psycopg2.Error) as error:
        print("Error al conectar a la base de datos:", error)
        return None

# Verifica el usuario y la clave en la base de datos
def verificar_usuario_y_clave(usuario, clave, connection):
    try:
        cursor = connection.cursor()
        consulta = f"SELECT * FROM usuarios WHERE nombre_usuario = '{usuario}' AND contraseña = '{clave}'"
        cursor.execute(consulta)
        registros = cursor.fetchall()
        if len(registros) > 0:
            print("Inicio de sesión exitoso.")
        else:
            print("Credenciales incorrectas.")
    except (Exception, psycopg2.Error) as error:
        print("Error al verificar las credenciales:", error)

if __name__ == "__main__":
    connection = conectar_base_de_datos()
    if connection:
        usuario = input("Ingresa tu usuario: ")
        clave = input("Ingresa tu clave: ")
        verificar_usuario_y_clave(usuario, clave, connection)
        connection.close()
