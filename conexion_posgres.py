import psycopg2

# try:
#     conexion=psycopg2.connect(database="base_prueba", user="postgres", password="bd2372")
#     cursor01=conexion.cursor()
#     cursor01.execute('select version()')
#     version=cursor01.fetchone()
# except Exception as err:
#     print('Erro al conectar a la base\n',err)
# else:
#     print(f'{version}')

# try:
#     cursor01.execute("insert into usuarios values(1004, 'Alan12','admin200')")
# except Exception as err:
#     print("Error al insertar datos",err)
# else:
#     print('Datos insertados correctamente')  

# conexion.commit()

##insertar datos y acceder a la base de datos del video que mande


## lo de abajo corresponde a la bd de la materia bd I, revisen el nombre de database como varia, asi distinguen cual es cual
## el try de abajo debe estar si o si, si lo comentan van a ver como las variables no quedan declaradas, lo mismo pasa si borran el print(f'{version})

try:
    conexion=psycopg2.connect(database="turnos", user="postgres", password="bd2372")
    cursor01=conexion.cursor()
    cursor01.execute('select version()')
    version=cursor01.fetchone()
except Exception as err:
    print('Erro al conectar a la base\n',err)
else:
    print(f'{version}')


cursor01.execute("select * from profesionales where dni_profesional>81000000 and genero_profesional = 'Femenino' ")
consulta = cursor01.fetchall()
print(consulta)     ##consultas sobre una base de datos que nos dieron en bd I

conexion.close()