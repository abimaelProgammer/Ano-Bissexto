Ano = int(input("Entre com o ano: "))

if Ano < 1582:
  print("Não está dentro do período do calendário Gregoriano")
elif Ano % 4 != 0:
  print("Não é um ano Bissexto")
elif Ano % 100 != 0:
  print("É um ano Bissexto: ")
elif Ano % 400!=0:
  print("Não é um ano Bissexto")
else:
  print("É um ano Bissexto")
