from enum import Enum

# --- ENUMERACIONES ---

class TipoIncidente(Enum):
    CAIDA_ARBOLES = "Caída de árboles"
    DESBORDAMIENTO_RIO = "Desbordamiento de río"
    BACHE = "Bache"
    ACCIDENTE = "Accidente"
    DERRUMBE = "Derrumbe"
    INCENDIO = "Incendio"
    OTRO = "Otro"

    @property
    def descripcion(self):
        return self.value

    @classmethod
    def desde_texto(cls, texto: str) -> "TipoIncidente":
        buscado = str(texto).strip().upper().replace(" ", "_")
        for tipo in cls:
            if buscado == tipo.name or str(texto).strip().lower() == tipo.value.lower():
                return tipo
        validos = ", ".join(t.name for t in cls)
        raise ValueError(f"Tipo de incidente inválido: '{texto}'. Valores válidos: {validos}")

    def __str__(self) -> str:
        return self.name

# FIN TipoIncidente


class Severidad(Enum):
    BAJA = "Baja"
    MEDIA = "Media"
    ALTA = "Alta"
    CRITICA = "Crítica"

    @property
    def descripcion(self):
        return self.value

    @classmethod
    def desde_texto(cls, texto):
        buscado = str(texto).strip().upper().replace(" ", "_")
        for severidad in cls:
            if buscado == severidad.name or str(texto).strip().lower() == severidad.value.lower():
                return severidad
        validos = ", ".join(s.name for s in cls)
        raise ValueError(f"Severidad inválida: '{texto}'. Valores válidos: {validos}")

    def __str__(self):
        return self.name

# FIN Severidad


class Estado(Enum):
    REPORTADO = "Reportado"
    EN_REVISION = "En revisión"
    EN_PROCESO = "En proceso"
    RESUELTO = "Resuelto"
    CERRADO = "Cerrado"

    @property
    def descripcion(self):
        return self.value

    @classmethod
    def desde_texto(cls, texto):
        buscado = str(texto).strip().upper().replace(" ", "_")
        for estado in cls:
            if buscado == estado.name or str(texto).strip().lower() == estado.value.lower():
                return estado
        validos = ", ".join(e.name for e in cls)
        raise ValueError(f"Estado inválido: '{texto}'. Valores válidos: {validos}")

    def __str__(self):
        return self.name

# FIN Estado


class Incidente:
    def __init__(self, id_incidente, titulo, descripcion, tipo: TipoIncidente, severidad: Severidad, estado: Estado = Estado.REPORTADO):
        self.id = id_incidente
        self.titulo = titulo
        self.descripcion = descripcion
        self.tipo = tipo
        self.severidad = severidad
        self.estado = estado

    def mostrar_detalle(self):
        """Muestra una tarjeta visual con la información completa del incidente."""
        print("\n" + "═" * 55)
        print(f" 📌  DETALLE DEL INCIDENTE #{self.id}")
        print("═" * 55)
        print(f" ▪ Título     : {self.titulo}")
        print(f" ▪ Descripción: {self.descripcion}")
        print(f" ▪ Tipo       : {self.tipo.descripcion}")
        print(f" ▪ Severidad  : ⚠️  {self.severidad.descripcion}")
        print(f" ▪ Estado     : 🔄 {self.estado.descripcion}")
        print("═" * 55 + "\n")

    def registrar(self):
        print(f"✅ [ÉXITO] Incidente #{self.id} registrado correctamente.")
        self.mostrar_detalle()

    def actualizar(self):
        print(f"⚙️  [ACTUALIZACIÓN] Datos del incidente #{self.id} modificados.")

    def cambiar_estado(self, nuevo_estado: Estado):
        if isinstance(nuevo_estado, str):
            nuevo_estado = Estado.desde_texto(nuevo_estado)
            
        estado_anterior = self.estado.descripcion
        self.estado = nuevo_estado
        
        print(f"🔄 [CAMBIO DE ESTADO] Incidente #{self.id}")
        print(f"      Anterior : {estado_anterior}")
        print(f"   👉 Nuevo    : {self.estado.descripcion}")
        print("-" * 55)


# --- MENÚ INTERACTIVO ---
def menu_interactivo():
    print("=" * 55)
    print("      📋 REGISTRO DE NUEVO INCIDENTE")
    print("=" * 55)
    
    # 1. Pedir datos básicos
    titulo = input("Título del incidente: ")
    descripcion = input("Descripción del incidente: ")

    # 2. Seleccionar Tipo
    print("\nTipos disponibles:")
    tipos_lista = list(TipoIncidente)
    for i, t in enumerate(tipos_lista, 1):
        print(f"  {i}. {t.descripcion}")
    opc_tipo = int(input("Selecciona el número de tipo: ")) - 1
    tipo_sel = tipos_lista[opc_tipo]

    # 3. Seleccionar Severidad
    print("\nSeveridades disponibles:")
    sev_lista = list(Severidad)
    for i, s in enumerate(sev_lista, 1):
        print(f"  {i}. {s.descripcion}")
    opc_sev = int(input("Selecciona el número de severidad: ")) - 1
    severidad_sel = sev_lista[opc_sev]

    # Crear el objeto Incidente
    incidente = Incidente(
        id_incidente=1,
        titulo=titulo,
        descripcion=descripcion,
        tipo=tipo_sel,
        severidad=severidad_sel
    )
    
    incidente.registrar()

    # 4. Ciclo para cambiar estados manualmente
    estados_lista = list(Estado)
    while True:
        print("\n¿Deseas cambiar el estado del incidente?")
        print("  0. Salir del programa")
        for i, est in enumerate(estados_lista, 1):
            print(f"  {i}. Cambiar a: {est.descripcion}")
            
        opcion = int(input("\nElige una opción: "))
        
        if opcion == 0:
            print("\n👋 ¡Programa finalizado!")
            break
        elif 1 <= opcion <= len(estados_lista):
            nuevo_est = estados_lista[opcion - 1]
            incidente.cambiar_estado(nuevo_est)
        else:
            print("⚠️ Opción inválida. Intenta de nuevo.")

if __name__ == "__main__":
    menu_interactivo()