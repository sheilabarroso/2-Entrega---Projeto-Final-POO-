class Cliente:
    def __init__(self, id_cliente: int, nome: str, email: str, cpf: str, enderecos: List[str]):
        self.id = id_cliente
        self.nome = nome
        self.email = email
        self.cpf = cpf
        self.enderecos = enderecos 
        self.ativo = True

    def atualizar_email(self, novo_email: str):
        if "@" not in novo_email:
            raise ValueError("Email inválido")
        self.email = novo_email

    def excluir(self):
        self.ativo = False

    def __str__(self):
        return f"Cliente {self.id} | {self.nome} | {self.email}"
