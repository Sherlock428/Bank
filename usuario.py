# Sistema Usuario
from dataclasses import dataclass

@dataclass
class Usuario:
    nome: str
    cpf: int
    senha: str
    credito: float
    chaves: list
    historico: list



@dataclass
class Transacao:
    descricao: str
    chave: int
    valor: float
    destinatario: Usuario
    remetente: Usuario


    def __str__(self):
        return f'''
{'=' * 30}
{'Comprovante Trasação'.center(30)}
{'=' * 30}

Valor: R${self.valor:.2f}
{'-' * 30}
Para: {self.destinatario.nome}
Chave: {self.chave}

Descrição: {self.descricao}
Remetente: {self.remetente.nome}
'''
        
