from conectapet.models.tutor import Tutor
from conectapet.models.veterinario import Veterinario
from conectapet.models.consulta import Consulta
from conectapet.models.animal import Animal
from conectapet.persistence.storage import salvar_linha, ler_linhas

class Clinica:
    def __init__(self, nome, cnpj):
        self.nome = nome
        self.cnpj = cnpj
        self.tutores = []
        self.veterinarios = []
        self.consultas = []

    def cadastrar_tutor(self, tutor):
        self.tutores.append(tutor)
        salvar_linha("dados/tutores.txt", tutor.to_txt())

    def cadastrar_veterinario(self, vet):
        self.veterinarios.append(vet)
        salvar_linha("dados/veterinarios.txt", vet.to_txt())

    def cadastrar_consulta(self, consulta):
        self.consultas.append(consulta)
        salvar_linha("dados/consultas.txt", consulta.to_txt())

    def listar_tutores(self):
        return [str(t) for t in self.tutores]

    def listar_veterinarios(self):
        return [str(v) for v in self.veterinarios]

    def listar_consultas(self):
        return [str(c) for c in self.consultas]