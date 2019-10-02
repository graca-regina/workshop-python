nota1 = float(input())
nota2 = float(input())
nota3 = float(input())
media = (nota1 + nota2 + nota3)/3.0
print('sua media é')
print(media)
if media >= 7.0:
    print('Aprovado')
elif media >= 5.0 or media < 7.0:
    print('Recuperação')
else:
    print('Reprovado')
