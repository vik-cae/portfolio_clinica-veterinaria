class Prescricao:
    def __init__(self, id_, descricao, medicamentos):
        self.id = id_
        self.descricao = descricao
        self.medicamentos = medicamentos  

    def __str__(self):
        meds = ", ".join(self.medicamentos)
        return f"Prescrição {self.id}: {self.descricao} - Medicamentos: {meds}"

    def to_txt(self):
        meds_str = ",".join(self.medicamentos)
        return f"{self.id}|{self.descricao}|{meds_str}"

    @classmethod
    def from_txt(cls, line):
        id_, descricao, meds_str = line.strip().split("|")
        medicamentos = meds_str.split(",")
        return cls(int(id_), descricao, medicamentos)
