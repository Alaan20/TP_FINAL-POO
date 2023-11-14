import psycopg2
from views.ventana import VentanaService

class ServiceDao:
    
    def __init__(self):
        self._conexion = psycopg2.connect(
            database = "[autosoft]",
            user= "postgres",
            password = "teclas",
            host="tpphost.duckdns.org",
            port = "5432")
        self._cursor = self._conexion.cursor()

    def get_all (self):
        self._cursor.execute("SELECT * FROM service")
        resu = self._cursor.fetchall()
        print(resu)
    
    def get_all_por_patente (self, patente):
        self._cursor.execute(f"SELECT * FROM service where patente='{patente}'")
        return self._cursor.fetchall()

    def get_by_id (self, id):
        self._cursor.execute(f"SELECT * FROM service where nro_service='{id.text()}' ")
        return self._cursor.fetchone()

    def commit (self, datos, patente):
        consulta = ""
        j = 0
        for i in datos:
            if j == 0:
                consulta += f"'{i}'"
                j = 1
            else:
                consulta += f",'{i}'"
        consulta += f",'{patente}'"
        if datos[0] == "Basico":
            campos = "tipo_service,luces_y_baul,amortiguadores,presion_neumaticos,tuerca_neumaticos,bateria,filtro_combustible,aceite_diferencial,aceite_y_filtro,patente"
        elif datos[0] == "Estandar":
            campos = "tipo_service,luces_y_baul,amortiguadores,presion_neumaticos,tuerca_neumaticos,bateria,filtro_combustible,aceite_diferencial,aceite_y_filtro,liquido,revision_liquido,bisagras_engrase,caño_de_escape,correa_direccion,airbag,inyeccion,sensores_actuadores,patente"
        
        elif datos[0] == "Completo":
            campos = "tipo_service,luces_y_baul,amortiguadores,presion_neumaticos,tuerca_neumaticos,bateria,filtro_combustible,aceite_diferencial,aceite_y_filtro,liquido,revision_liquido,bisagras_engrase,caño_de_escape,correa_direccion,airbag,inyeccion,sensores_actuadores,cinturon_seguridad,climatizacion,historial_fallas,instrumental,escaneo_computadora,patente"
        print(campos)
        print(f"{consulta}")
        self._cursor.execute(f"INSERT INTO service ({campos}) VALUES ({consulta})")
        self._conexion.commit()