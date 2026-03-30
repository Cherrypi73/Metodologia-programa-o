from util.data import Data

investimentos = []


def get_investimentos():
    return investimentos


def inserir_investimento(investimento):
    investimentos.append(investimento)


class Investimento:
    def __init__(self, data, emissor, id, tipo, validade, rentabilidade, status):
        self.data = data
        self.emissor = emissor
        self.id = id
        self.tipo = tipo if tipo in ('renda_fixa', 'renda_váriavel', 'híbrida') else 'indefinida'
        self.validade = validade
        self.rentabilidade = rentabilidade
        self.status = status


    def __str__(self):
        data_emissão = Data(dia=21, mês=11, ano=2026)
        formato = '{:<7} {:<10}{:<4} {:<15} {:<9} {:<5} {:<10}'
        investimento_formatado = formato.format( str(self.data.calcular_idade(data_referência=data_emissão)) + ' anos',
                                                self.emissor,
                                                self.id,
                                                self.tipo,
                                                self.validade,
                                                self.rentabilidade,
                                                'status' if self.status else '')
        return investimento_formatado
