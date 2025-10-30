from conectapet.models.prescricao import Prescricao


class Consulta:
    def __init__(self, id_, data, descricao, veterinario, animal):
        self.id = id_
        self.data = data
        self.descricao = descricao
        self.veterinario = veterinario
        self.animal = animal
        self.prescricao = None  

    def registrar_prescricao(self, prescricao):
        self.prescricao = prescricao

    def __str__(self):
        return f"Consulta {self.id}: {self.data} - {self.animal.nome} com {self.veterinario.nome}"

    def to_txt(self):
        presc_id = self.prescricao.id if self.prescricao else "None"
        return f"{self.id}|{self.data}|{self.descricao}|{self.veterinario.id}|{self.animal.id}|{presc_id}"

    @classmethod
    def from_txt(cls, line):
        id_, data, descricao, vet_id, animal_id, presc_id = line.strip().split("|")
        # Obs: o veterinário e o animal serão associados depois pelo controller
        return cls(int(id_), data, descricao, vet_id, animal_id)