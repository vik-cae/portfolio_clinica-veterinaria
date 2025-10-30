class Animal:
    def __init__(self, id_, nome, especie, raca, idade):
        self.id = id_
        self.nome = nome
        self.especie = especie
        self.raca = raca
        self.idade = idade

    def __str__(self):
        return f"{self.nome} ({self.especie}, {self.raca}) - {self.idade} anos"

    def to_txt(self):
        return f"{self.id}|{self.nome}|{self.especie}|{self.raca}|{self.idade}"

    @classmethod
    def from_txt(cls, line):
        id_, nome, especie, raca, idade = line.strip().split("|")
        return cls(int(id_), nome, especie, raca, int(idade))
