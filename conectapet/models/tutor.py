from models.pessoa import Pessoa


class Tutor(Pessoa):
    def __init__(self, id_, nome, telefone, email, cpf, endereco):
        super().__init__(id_, nome, telefone, email)
        self.cpf = cpf
        self.endereco = endereco
        self.animais = []  

    def adicionar_animal(self, animal):
        self.animais.append(animal)

    def listar_animais(self):
        return [a.nome for a in self.animais]

    def __str__(self):
        return f"Tutor: {self.nome} - CPF: {self.cpf}"

    def to_txt(self):
        return f"{self.id}|{self.nome}|{self.telefone}|{self.email}|{self.cpf}|{self.endereco}"

    @classmethod
    def from_txt(cls, line):
        id_, nome, telefone, email, cpf, endereco = line.strip().split("|")
        return cls(int(id_), nome, telefone, email, cpf, endereco)
