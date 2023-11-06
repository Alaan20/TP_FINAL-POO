import psycopg2

class AutoDao:
    
    def __init__(self):
        self._conexion = psycopg2.connect(
            database = "tp_final_poo",
            user= "postgres",
            password = "bd2372",
            port = "5432")
        self._cursor = self._conexion.cursor()

    def get_all (self):
        self._cursor.execute("SELECT * FROM autos")
        resu = self._cursor.fetchall()
        print(resu)
    
    def get_one (self, patente):
        self._cursor.execute(f"SELECT * FROM autos where patente='{patente}'")
        return self._cursor.fetchone()
        # print(resu)

    def commit (self, datos):
        # self._cursor.execute()
        # self.commit()
        pass