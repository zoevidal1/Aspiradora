class AspiradoraConEstados:
    def __init__(self):
        self.posicion = "A"
        self.limpio_a = False  # Atributo que indica si la posición A está limpia
        self.limpio_b = False  # Atributo que indica si la posición B está limpia

    def aspirar(self):
        if self.posicion == "A":
            self.limpio_a = True  # Se marca como limpia la posición A
            print("Se aspiró la posición A")
        elif self.posicion == "B":
            self.limpio_b = True  # Se marca como limpia la posición B
            print("Se aspiró la posición B")

    def derecha(self):
        self.posicion = "B"
        print("Se movió a la posición B")

    def izquierda(self):
        self.posicion = "A"
        print("Se movió a la posición A")

    def actuar(self):
        if self.posicion == "A" and not self.limpio_a:
            self.aspirar()
        elif self.posicion == "B" and not self.limpio_b:
            self.aspirar()
        elif self.posicion == "A" and self.limpio_a:
            self.derecha()
        elif self.posicion == "B" and self.limpio_b:
            self.izquierda()

asp = AspiradoraConEstados()

while not (asp.limpio_a and asp.limpio_b):
    asp.actuar()
