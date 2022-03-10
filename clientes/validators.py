import re
from validate_docbr import CPF

def cpf_valido(cpf):
    valida_cpf = CPF()
    return valida_cpf.validate(cpf)

def nome_valido(nome):
    return nome.isalpha()

def rg_valido(rg):
    return len(rg) == 9

def celular_valido(celular):
    '''Verifica se o celular é válido (11 91234-1234)'''
    modelo = '[0-9]{2} 9[0-9]{4}-[0-9]{4}'
    reposta = re.findall(modelo, celular)
    return reposta
