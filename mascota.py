"""Fase 1.2 - Clases y atributos POO de la mascota virtual."""
from dataclasses import dataclass, field
from time import time


@dataclass
class Estado:
    alimentacion: float = 70
    diversion: float = 70
    presencia: float = 70

    def _limitar(self, v):
        return max(0, min(100, v))

    def cambiar(self, alimentacion=0, diversion=0, presencia=0):
        self.alimentacion = self._limitar(self.alimentacion + alimentacion)
        self.diversion = self._limitar(self.diversion + diversion)
        self.presencia = self._limitar(self.presencia + presencia)

    def promedio(self):
        return (self.alimentacion + self.diversion + self.presencia) / 3


@dataclass
class Item:
    nombre: str
    precio: int
    efecto_alimentacion: float = 0
    efecto_diversion: float = 0
    efecto_presencia: float = 0

# Catálogo global en el backend
TIENDA = {
    "manzana": Item("Manzana", precio=10, efecto_alimentacion=15),
    "pizza": Item("Pizza", precio=25, efecto_alimentacion=40, efecto_diversion=5),
    "pelota": Item("Pelota", precio=15, efecto_diversion=30),
}

@dataclass
class Mascota:
    nombre: str = "Mascota"
    monedas: int = 50  # Monedas iniciales
    inventario: dict = field(default_factory=lambda: {"manzana": 1})
    estado: Estado = field(default_factory=Estado)
    ultima_visita: float = field(default_factory=time)
    historial: list = field(default_factory=list)  # memoria de interacciones (usar en Fase 2 con la IA)

    # Costos de las acciones
    COSTO_ALIMENTAR = 10
    COSTO_JUGAR = 5

    def animo(self):
        p = self.estado.promedio()
        return "feliz" if p > 66 else "normal" if p > 42 else "triste" if p > 20 else "abandonada"

    def _registrar(self, evento):
        self.historial.append({"evento": evento, "t": time(), "animo": self.animo()})
        self.ultima_visita = time()

    def alimentar(self) -> bool:
        if self.monedas >= self.COSTO_ALIMENTAR:
            self.monedas -= self.COSTO_ALIMENTAR
            self.estado.cambiar(alimentacion=25, presencia=4)
            return True
        return False

    def jugar(self) -> bool:
        if self.monedas >= self.COSTO_JUGAR:
            self.monedas -= self.COSTO_JUGAR
            self.estado.cambiar(diversion=25, alimentacion=-5, presencia=4)
            return True
        return False

    def ganar_monedas(self, cantidad: int):
        self.monedas += cantidad

    def comprar_item(self, id_item: str) -> bool:
        if id_item not in TIENDA:
            return False
        item = TIENDA[id_item]
        if self.monedas >= item.precio:
            self.monedas -= item.precio
            self.inventario[id_item] = self.inventario.get(id_item, 0) + 1
            return True
        return False

    def usar_item(self, id_item: str) -> bool:
        if self.inventario.get(id_item, 0) > 0:
            item = TIENDA[id_item]
            self.inventario[id_item] -= 1
            self.estado.cambiar(
                alimentacion=item.efecto_alimentacion,
                diversion=item.efecto_diversion,
                presencia=item.efecto_presencia
            )
            return True
        return False

    def acompanar(self):
        self.estado.cambiar(presencia=20)
        self._registrar("acompanar")

    def pasar_tiempo(self):
        """Descuenta estado según los minutos que estuvo sola."""
        minutos = (time() - self.ultima_visita) / 60
        self.estado.cambiar(-minutos * 0.5, -minutos * 0.4, -minutos * 0.6)
