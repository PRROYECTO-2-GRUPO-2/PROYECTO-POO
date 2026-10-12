class Usuario:
    def __init__(self, id_usuario: int, nombre: str, correo: str, contrasena: str, activo: bool = True):
        self.id = id_usuario
        self.nombre = nombre
        self.correo = correo
        self.contrasena = contrasena
        self.activo = activo

    def iniciar_sesion(self, correo: str, contrasena: str) -> bool:
        if self.correo == correo and self.contrasena == contrasena:
            if self.activo:
                print(f"Sesión iniciada correctamente para el usuario: {self.nombre}")
                return True
            else:
                print(f"El usuario {self.nombre} está inactivo.")
                return False
        else:
            print("Credenciales incorrectas.")
            return False

    def registrar_incidente(self, incidente) -> None:
        if self.activo:
            incidente.registrar()
            print(f"El usuario {self.nombre} registró el incidente {incidente.id}.")
        else:
            print(f"El usuario {self.nombre} no puede registrar incidentes porque está inactivo.")

    def __str__(self) -> str:
        return f"Usuario({self.id}): {self.nombre} <{self.correo}>"

# FIN Usuario