class Produto:
    def __init__(self, sku: str, nome: str, categoria: str, preco_unitario: float, estoque: int):
        self.sku = sku
        self.nome = nome
        self.categoria = categoria
        self.preco_unitario = preco_unitario
        self.estoque = estoque
        self.ativo = True
        
    @property
    def preco_unitario(self):
        return self._preco_unitario

    @preco_unitario.setter
    def preco_unitario(self, valor):
        if valor <= 0:
            raise ValueError("Preço deve ser maior que zero")
        self._preco_unitario = valor

    @property
    def estoque(self):
        return self._estoque

    @estoque.setter
    def estoque(self, valor):
        if valor < 0:
            raise ValueError("Estoque não pode ser negativo")
        self._estoque = valor
    
    def atualizar(self, preco: float = None, estoque: int = None):
        if preco is not None:
            self.preco_unitario = preco

        if estoque is not None:
            self.estoque = estoque
            
    def __eq__(self, other):
        return self.sku == other.sku

    def __lt__(self, other):
        return self.preco_unitario < other.preco_unitario

    def __str__(self):
        return f"[{self.sku}] {self.nome} | R$ {self.preco_unitario:.2f} | Estoque: {self.estoque}"
