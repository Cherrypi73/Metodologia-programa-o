from util.data import Data

consultoras = []


def get_consultoras():
    return consultoras


def inserir_consultora(consultora):
    consultoras.append(consultora)


class Consultora:
    def __init__(self, nome, data_registro, orçamento, endereço, telefone):
        self.nome = nome
        self.data_registro = data_registro
        self.orçamento = orçamento
        self.endereço = endereço
        self.telefone = telefone

    def __str__(self):
        formato = '{:<14} {:<11} {:<10} {:<20} {:<10}'
        consultora_formatada = formato.format(self.nome,
                                              str(self.data_registro),
                                              self.orçamento,
                                              self.endereço,
                                              self.telefone)
        return consultora_formatada
