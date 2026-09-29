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
class Mascota:
    nombre: str = "Mascota"
    estado: Estado = field(default_factory=Estado)
    ultima_visita: float = field(default_factory=time)
    historial: list = field(default_factory=list)  # memoria de interacciones (usar en Fase 2 con la IA)

    def animo(self):
        p = self.estado.promedio()
        return "feliz" if p > 66 else "normal" if p > 42 else "triste" if p > 20 else "abandonada"

    def _registrar(self, evento):
        self.historial.append({"evento": evento, "t": time(), "animo": self.animo()})
        self.ultima_visita = time()

    def alimentar(self):
        self.estado.cambiar(alimentacion=25, presencia=4)
        self._registrar("alimentar")

    def jugar(self):
        self.estado.cambiar(diversion=25, alimentacion=-5, presencia=4)
        self._registrar("jugar")

    def acompanar(self):
        self.estado.cambiar(presencia=20)
        self._registrar("acompanar")

    def pasar_tiempo(self):
        """Descuenta estado según los minutos que estuvo sola."""
        minutos = (time() - self.ultima_visita) / 60
        self.estado.cambiar(-minutos * 0.5, -minutos * 0.4, -minutos * 0.6)
