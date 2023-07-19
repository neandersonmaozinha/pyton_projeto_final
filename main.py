import requests

from acessando_cep import BuscaEndereco
cep = input("Digite um cep: \n")
objeto_cep = BuscaEndereco(cep)

# r = requests.get("https://viacep.com.br/ws/01001000/json/")
# print(r.text)
a = objeto_cep.acessa_via_cep()
bairro, logradouro, cidade, uf, cep = objeto_cep.acessa_via_cep()


print("O cep {} digitado corresponde a CIDADE DE: {}, ao BAIRRO de: {}, a UF de: {}, RUA {}   ".format(cep, logradouro, bairro, cidade, uf))