import os,random

from asciiart import titulo,fim, titulo_menu, titulo_paises, titulo_animais, titulo_filmes ,passo1, passo2, passo3, passo4, passo5, passo_final, salvo, salvo_rapido, salvo_perfeito

from forca_func import carrega_tema, remove_caracteres, sorteio, forca

#INICIO DO JOGO

limite_erros=6
while True:  
   erros=0
   tema=0
   passos=""
   letras=[]
   lista_letras=[]
   os.system("cls")
   print(f"\n{titulo}")
   resposta=input(titulo_menu) 
   while resposta != {"1","2","3","x","X"}:
      if resposta=="1":
         tema="paises"
         lista=carrega_tema(tema)
         titulo_tema=titulo_paises
         break
      if resposta=="2":
         tema="animais"
         lista=carrega_tema(tema)
         titulo_tema=titulo_animais
         break
      if resposta=="3":
         tema="filmes"
         lista=carrega_tema(tema)
         titulo_tema=titulo_filmes
         break
      if resposta=="x" or resposta=="X":
         print("\n=== Fim do jogo ===")
         exit()
      os.system("cls")
      print(f"\n{titulo}")
      resposta=input(titulo_menu)
   palavra_sorteada,subtraco,tam_subtraco,subtraco_vazio=sorteio(lista)
   os.system("cls")
   print(f"\n{titulo}{titulo_tema}")
   print(f"\n{subtraco_vazio.upper()}   ===> LETRAS ERRADAS: {lista_letras}")
   while True:
      letra=input("\nDigite uma letra: ").upper()
      if len(letra)==1 and letra.isnumeric()==False:
         res=forca(palavra_sorteada,letra,subtraco)
         resultado=remove_caracteres(res)
         if letra not in palavra_sorteada and letra not in letras:
            erros=erros+1
            if erros==1:
               passos=passo1
            if erros==2:
               passos=passo2
            if erros==3:
               passos=passo3
            if erros==4:
               passos=passo4
            if erros==5:
               passos=passo5
            if erros==6:
               passos=passo_final
            letras.append(letra)
            lista_letras=remove_caracteres(letras)
         print(f"\n{titulo}{titulo_tema}")
         print(f"\n{resultado.upper()}   ===> LETRAS ERRADAS: {lista_letras} {passos}")
         if erros==limite_erros:
            print(fim)
            print(f"==== {palavra_sorteada} ===")
            y=input("\nENTER PARA VOLTAR AO MENU......")
            break
         tam_subtraco = resultado.count("_")
         if resultado.count("_") == 0:
            if len(letras) >= 4:
               print(salvo)
            if len(letras) >= 1 and len(letras) < 4:
               print(salvo_rapido)
            if len(letras) == 0:
               print(salvo_perfeito)
            y=input("ENTER PARA VOLTAR AO MENU...")  
            break
      else:
         print("\nDigite somente uma letra....")         
      
 







