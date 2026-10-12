class Rol:
    def __init__(self, id_rol: int, nombre: str, descripcion: str):
        self.id = id_rol
        self.nombre = nombre
        self.descripcion = descripcion

    @property
    def info(self) -> str:
        return f"{self.nombre}: {self.descripcion}"

    @classmethod
    def desde_texto(cls, texto: str) -> "Rol":
        buscado = str(texto).strip()
        if not buscado:
            raise ValueError("El texto del rol no puede estar vacío.")
        return cls(id_rol=0, nombre=buscado, descripcion="Rol asignado por sistema")

    def __str__(self) -> str:
        return self.nombre
    
mi_rol = Rol.desde_texto("Administrador")
print(mi_rol)    
    