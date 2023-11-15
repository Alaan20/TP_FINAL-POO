from database.database import DataBase

class ServiceDb:
    def __init__(self):
        self.base = DataBase()
        
    def leer_service(self,patente):
        return self.base.getAll(f"SELECT * FROM service WHERE patente = '{patente}'")
    
    def get_all_por_patente (self, patente):
        return self.base.getAll(f"SELECT * FROM servicios WHERE patente = '{patente}'")
    
    def get_by_id(self,id):
        return self.base.get(f"SELECT * FROM service WHERE nro_service = {id.text()}")
    
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
        
        return self.base.query(f"INSERT INTO service ({campos}) VALUES ({consulta})")