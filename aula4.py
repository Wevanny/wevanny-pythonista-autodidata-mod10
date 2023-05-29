'''
# Regex ou Regular Expression:
* De forma geral, o regex é como se fosse uma forma de encontrar, substituir, e extrair um caracter ou uma
sequência de caracteres. 
'''
# CARACTERE - Qualquer letra, dígito ou símbolo no padrão.
import re

hey = 'carol@gmail.com.br'
# Findall -> Retorna todas as ocorrências.
result = re.findall(r"(@.{1,8}\.)", hey)
print(result)
# Search -> Retorna a ocorrência de um regex dentro de uma string
result = re.search(r"(@.{1,8}\.)", hey)
print(result)
# Split -> Separar partes de uma string.
result = re.split(r"(@.{1,8}\.)", hey)
print(result)
# Sub -> Substitui partes de uma string.
result = re.sub(r"(@.{1,8}\.)", '@yahoo.', hey)
print(result)