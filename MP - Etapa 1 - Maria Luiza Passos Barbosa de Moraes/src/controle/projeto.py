from util.gerais import imprimir_objetos
from util.data import Data
from entidades.consultora import Consultora, inserir_consultora, get_consultoras
from entidades.investimento import Investimento, inserir_investimento, get_investimentos


def cadastrar_investimentos():
    inserir_investimento(Investimento(Data(dia=7, mês=10, ano=2025), 'Bb' ,23,'renda_fixa', '1 ano', 0.1,  True))
    inserir_investimento(Investimento(Data(dia=8, mês=1, ano=2026), 'Bradesco',36 ,'renda_fixa', '31 dias', 0.01,  False))
    inserir_investimento(Investimento(Data(dia=2, mês=1, ano=2025, ), 'Caixa',34 ,'híbrida', '6 meses', 0.23, True))
    inserir_investimento(Investimento(Data(dia=11, mês=8, ano=2025), 'BB', 20,'renda_váriavel', '3 meses', 0.18, False))


def cadastrar_consultoras():
    inserir_consultora(Consultora('Aura Invest', Data(9, 10, 2021), 136000000, 'Rua Brilhante', '6799864532'))
    inserir_consultora(Consultora('Nexum Invest', Data(17, 1, 2024), 136500000, 'Rua Lopes', '1018876541'))
    inserir_consultora(Consultora('Eixo Finanças', Data(29, 3, 2015), 136300000, 'Rua Avenida Paulista', '679989032'))
    inserir_consultora(Consultora('Aura Invest', Data(12, 5, 2008), 129300000, 'Rua Brilhante', '6799864532'))


if __name__ == '__main__':
    print('\nConsultoria de investimentos 2026')
    cadastrar_investimentos()
    imprimir_objetos(cabeçalho='Investimento : data, emissor, id, tipo, validade, rentabilidade, status',
                     objetos=get_investimentos())
    cadastrar_consultoras()
    imprimir_objetos('Consultora: nome, data_registro, orçamento, endereço, telefone', get_consultoras())
