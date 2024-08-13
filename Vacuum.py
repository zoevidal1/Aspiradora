class AgenteReactivoConEstados:
    def __init__(self):
        self.estado_anterior = None
        self.estado_actual = "Sucio"  # Suponemos que todo está sucio al principio

    def actualizar_estado(self, estado_actual):
        # Solo actualizamos el estado si se aspira
        if estado_actual == "Sucio":
            self.estado_actual = "Limpio"
        else:
            self.estado_actual = estado_actual

    def decidir_accion(self):
        if self.estado_actual == "Sucio":
            return "Aspirar"
        elif self.estado_actual == "Izquierda" and self.estado_anterior != "Izquierda":
            return "Mover derecha"
        elif self.estado_actual == "Derecha" and self.estado_anterior != "Derecha":
            return "Mover izquierda"
        elif self.estado_actual == "Limpio":
            return "Moverse"  # Continúa al siguiente estado
        else:
            return "Nada que hacer"

# Uso del agente
agente = AgenteReactivoConEstados()
estados = ["Derecha", "Izquierda", "Sucio", "Limpio"]

for estado in estados:
    accion = agente.decidir_accion()
    print(f"Estado anterior agente: {agente.estado_anterior}")
    agente.actualizar_estado(estado)
    print(f"Estado actual: {agente.estado_actual}, Acción: {accion}")
    agente.estado_anterior = agente.estado_actual  # Actualizamos el estado anterior después de la acción
