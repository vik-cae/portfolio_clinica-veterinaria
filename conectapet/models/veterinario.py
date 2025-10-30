from models.pessoa import Pessoa

class Veterinario(Pessoa):
    def __init__(self, id_, nome, telefone, email, crmv, especialidade):
        super().__init__(id_, nome, telefone, email)
        self.crmv = crmv
        self.especialidade = especialidade

    def __str__(self):
        return f"Veterinário: {self.nome} - {self.especialidade}"

    def to_txt(self):
        return f"{self.id}|{self.nome}|{self.telefone}|{self.email}|{self.crmv}|{self.especialidade}"

    @classmethod
    def from_txt(cls, line):
        id_, nome, telefone, email, crmv, especialidade = line.strip().split("|")
        return cls(int(id_), nome, telefone, email, crmv, especialidade)