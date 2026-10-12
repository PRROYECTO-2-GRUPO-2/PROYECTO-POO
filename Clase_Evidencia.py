from datetime import datetime

class Evidencia:
    def __init__(self, id: int, tipo_archivo: str, fecha_subida: datetime):
        self.id = id
        self.tipo_archivo = tipo_archivo
        self.fecha_subida = fecha_subida

    def subir(self):
        print(f"Se ha subido la evidencia {self.id}")