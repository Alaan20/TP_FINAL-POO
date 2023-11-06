import psycopg2
from Vista.ventana import VentanaService

class ServiceDao:
    
    def __init__(self):
        self._conexion = psycopg2.connect(
            database = "tp_final_poo",
            user= "postgres",
            password = "bd2372",
            port = "5432")
        self._cursor = self._conexion.cursor()

    def get_all (self):
        self._cursor.execute("SELECT * FROM service")
        resu = self._cursor.fetchall()
        print(resu)
    
    def get_all_por_patente (self, patente):
        self._cursor.execute(f"SELECT * FROM service where patente='{patente}'")
        return self._cursor.fetchall()

    def commit (self, datos, patente):
        consulta = ""
        j = 0
        for i in datos:
            if j == 0:
                consulta += f"'{i}'"
                j = 1
            else:
                consulta += f",'{i}'"
        print(consulta)
        if datos[0] == "Basico":
            campos = "tipo_service,amortiguadores,presion_neumaticos,tuerca_neumaticos,luces_y_baul,bateria,aceite_y_filtro,aceite_diferencial,filtro_combustible,patente"
            print(campos)
            self._cursor.execute(f"INSERT INTO service ({campos}) VALUES ({consulta},'{patente}')")
            self._conexion.commit()
        #elif len(datos) == 16:
        #    campos = "tipo_service,amortiguadores,presion_neumaticos,tuerca_neumaticos,Luces y baul,bateria,aceite_y_filtro,aceite_diferencial,filtro_combustible,liquido,revision_liquido,bisagras_engrase,caño_de_escape,correa_direccion,airbag,inyeccion,sensores_actuadores,patente"
        ##16 en adelante no utilizar
        #else:
        #    #cinturon_seguridad,climatizacion,historial_fallas,instrumental,escaneo_computadora,patente"