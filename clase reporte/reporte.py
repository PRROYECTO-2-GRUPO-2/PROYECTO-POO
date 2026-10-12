from datetime import datetime


class Reporte:

    def __init__(
        self,
        id_reporte: int,
        tipo: str,
        fecha_generacion: datetime,
        formato: str,
    ):
        self.__id = id_reporte
        self.__tipo = tipo 
        self.__fecha_generacion = fecha_generacion
        self.__formato = formato


    @property
    def id(self) -> int:
        return self.__id

    @property
    def tipo(self) -> str:
        return self.__tipo

    @tipo.setter
    def tipo(self, nuevo_tipo: str):
        self.__tipo = nuevo_tipo

    @property
    def fecha_generacion(self) -> datetime:
        return self.__fecha_generacion

    @fecha_generacion.setter
    def fecha_generacion(self, nueva_fecha: datetime):
        self.__fecha_generacion = nueva_fecha

    @property
    def formato(self) -> str:
        return self.__formato

    @formato.setter
    def formato(self, nuevo_formato: str):
        self.__formato = nuevo_formato


    def generar(self):
        """Genera el contenido del reporte."""
        print(
            f"Generando reporte de tipo '{self.__tipo}' con ID: {self.__id}..."
        )

    def exportar(self):
        """Exporta el reporte al formato especificado."""
        print(f"Exportando reporte {self.__id} en formato {self.__formato}...")


if __name__ == "__main__":
    mi_reporte = Reporte(
        id_reporte=1,
        tipo="Ventas Mensuales",
        fecha_generacion=datetime.now(),
        formato="PDF",
    )

    mi_reporte.generar()
    mi_reporte.exportar()