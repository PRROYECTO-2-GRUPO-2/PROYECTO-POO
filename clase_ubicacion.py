class Ubicacion:
    # Contador para generar el ID de forma automática
    _contador_id = 0

    def __init__(self, direccion: str, latitud: float = None, longitud: float = None):
        # Cada vez que se crea una ubicación, el ID aumenta en 1
        Ubicacion._contador_id += 1
        self.id = Ubicacion._contador_id
        self.direccion = direccion.strip()
        self.latitud = latitud
        self.longitud = longitud

    # Funcion para obtener los valores de los atributos
    def get_id(self) -> int:
        return self.id

    def get_direccion(self) -> str:
        return self.direccion

    # Funcion para mostrar la información adaptándose si tiene o no coordenadas
    def __str__(self) -> str:
        if self.latitud is not None and self.longitud is not None:
            return f"📍 [Ubicación #{self.id}] {self.direccion} | Coordenadas: ({self.latitud}, {self.longitud})"
        else:
            return f"📍 [Ubicación #{self.id}] {self.direccion} (Registrado por Referencia)"


# --- Menú principal interactivo del sistema ---
if __name__ == "__main__":
    # Lista para almacenar las ubicaciones que vayamos registrando
    ubicaciones_registradas = []

    while True:
        print("\n=============================================")
        print("   RESGISTRO DE LA UBICACION DEL INCIDENTE  ")
        print("=============================================")
        print("1. Registrar ubicación por Referencia (Recomendado)")
        print("2. Registrar ubicación por Coordenadas Exactas (Manual)")
        print("3. Ver todas las ubicaciones registradas")
        print("4. Salir")
        
        opcion = input("\nSeleccione una opción (1-4): ")

        if opcion == "1":
            print("\n--- REGISTRO GUIADO POR REFERENCIA ---")
            
            # Datos obligatorios para ubicar la zona general
            departamento = input("Ingrese el Departamento (ej. San Salvador, La Libertad): ")
            municipio = input("Ingrese el Municipio / Pueblo / Cantón (ej. Santa Tecla, Soyapango): ")
            
            # Dato opcional para dar mayor detalle de la ubicación
            calle_avenida = input("Ingrese la Calle, Avenida o Pasaje (Opcional - Presione Enter para omitir): ")
            
            # Referencia clave del lugar del incidente
            referencia = input("Ingrese el punto de referencia (ej. Frente a la Biblioteca Nacional): ")
            
            # Aqui se arma la dirección limpia uniendo solo los campos que se llenaron
            elementos_direccion = []
            if calle_avenida.strip():
                elementos_direccion.append(calle_avenida.strip())
            
            elementos_direccion.append(referencia.strip())
            elementos_direccion.append(municipio.strip())
            elementos_direccion.append(departamento.strip())
            elementos_direccion.append("El Salvador")
            
            # Aqui se unen los elementos separados por comas
            direccion_completa = ", ".join(elementos_direccion)
            
            # objeto solo con la dirección (sin coordenadas)
            nueva = Ubicacion(direccion=direccion_completa)
            ubicaciones_registradas.append(nueva)
            
            print(f"\n✅ ¡Ubicación registrada con éxito!")

        elif opcion == "2":
            try:
                print("\n--- REGISTRO MANUAL DE COORDENADAS ---")
                lat = float(input("Ingrese la latitud exacta (ej. 13.6929): "))
                lon = float(input("Ingrese la longitud exacta (ej. -89.2182): "))
                dir_texto = input("Ingrese una breve descripción o nombre del lugar: ")
                
                # objeto con latitud y longitud reales ingresadas por el usuario
                nueva = Ubicacion(direccion=dir_texto, latitud=lat, longitud=lon)
                ubicaciones_registradas.append(nueva)
                
                print(f"\n✅ ¡Ubicación registrada con éxito!")
            except ValueError:
                print("\n[Error]: Asegúrese de ingresar números válidos para la latitud y la longitud.")

        elif opcion == "3":
            print("\n=== HISTORIAL DE UBICACIONES REGISTRADAS ===")
            if not ubicaciones_registradas:
                print("No hay ubicaciones registradas todavía.")
            else:
                for u in ubicaciones_registradas:
                    print(u)

        elif opcion == "4":
            print("\nSaliendo del sistema de ubicaciones.")
            break
        else:
            print("\n[Error]: Opción no válida. Intente de nuevo.")