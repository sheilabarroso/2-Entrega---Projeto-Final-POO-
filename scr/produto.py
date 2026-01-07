class Produto:
    def __init__(self, sku: str, nome: str, categoria: str, preco_unitario: float, estoque: int):
        if preco_unitario < 0:
            raise ValueError ("Preço não pode ser negativo")
        if estoque < 0:
            raise ValueError ("Estoque não pode ser negativo")

        self.sku = sku
        self.nome = nome
        self.categoria = categoria
        self.preco_unitario = preco_unitario
        self.estoque = estoque
        self.ativo = True

    def atualizar(self, preco: float = None, estoque: int = None):
        if preco is not None:
            if preco < 0:
                raise ValueError("Preço inválido")
            self.preco_unitario = preco

        if estoque is not None:
            if estoque < 0:
                raise ValueError("Estoque inválido")
            self.estoque = estoque

    def baixar_estoque(self, quantidade: int):
        if quantidade > self.estoque:
            raise ValueError("Estoque insuficiente")
        self.estoque -= quantidade

    def repor_estoque(self, quantidade: int):
        self.estoque += quantidade

    def excluir(self):
        self.ativo = False

    def __str__(self):
        return f"[{self.sku}] {self.nome} | R$ {self.preco_unitario:.2f} | Estoque: {self.estoque}"
