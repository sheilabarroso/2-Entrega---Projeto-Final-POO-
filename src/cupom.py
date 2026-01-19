from datetime import datetime

class Cupom:
    def __init__(self, codigo, tipo, valor, validade):
        self.codigo = codigo
        self.tipo = tipo.upper()
        self.valor = valor
        self.validade = datetime.strptime(validade, "%Y-%m-%d")

    def esta_valido(self):
        return datetime.now() <= self.validade

    def calcular_desconto(self, subtotal):
        if not self.esta_valido():
            return 0.0

        if self.tipo == "PERCENTUAL":
            return subtotal * (self.valor / 100)

        if self.tipo == "VALOR":
            return min(self.valor, subtotal)

        return 0.0

