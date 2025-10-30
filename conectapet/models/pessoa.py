class Pessoa:
    def __init__(self, id_, nome, telefone, email):
        self.id = id_
        self.nome = nome
        self.telefone = telefone
        self.email = email

    def __str__(self):
        return f"{self.id} - {self.nome} ({self.email})"

    def to_txt(self):
        return f"{self.id}|{self.nome}|{self.telefone}|{self.email}"

    @classmethod
    def from_txt(cls, line):
        id_, nome, telefone, email = line.strip().split("|")
        return cls(int(id_), nome, telefone, email)
