import os, random

# FUNÇOES

#cria e retorna uma lista com o tema escolhido
def carrega_tema(tema):
   lista=[]
   with open(tema+".txt", encoding='utf-8', mode='r') as arquivo:
      for linha in arquivo:
         linha=linha.upper()
         lista.append(linha.rstrip())
      return lista

#remove caracteres indesejaveis do subtraço e resultado
def remove_caracteres(sub):
   sub1=str(sub)
   subtraco=sub1.replace(",","").replace("'","").replace("[","").replace("]","")
   return subtraco

#sorteia uma palavra da lista do tema, cria um subtraço vazio de acordo com o num de letras da palavra
def sorteio(lista):
   subtraco=[]
   sorteio = random.randint(1,len(lista))
   palavra_sorteada=lista[sorteio-1]
   num_letras=len(palavra_sorteada)
   for letra in palavra_sorteada:
      if letra==" ":
         subtraco.append(" ")
      else:
         subtraco.append("__")
   subtraco_vazio=remove_caracteres(subtraco)
   tam_subtraco=len(subtraco_vazio)
   return palavra_sorteada,subtraco,tam_subtraco,subtraco_vazio

#verifica se acertou a letra e retorna o sutraço preenchido 
def forca(palavra_sorteada,letra,subtraco):
   os.system("cls")
   for index, valor in enumerate(palavra_sorteada):
      if valor == letra:
         subtraco[index]=valor
   return subtraco