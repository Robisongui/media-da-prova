#montar um programa quereceba tres notas e calcule a media.
#programa principal
#materia python
print("programa que calcula a media da diciplina de python")
nt_exerc = float(input("digite qual foi a media dos execicios:"))
nt_avdis = float(input("digite qual foi a nota da prova dissertativa:"))
nt_prova = float(input("digite qual foi a nota da prova:"))
#processamento
media = (nt_exerc + nt_avdis + nt_prova ) /3
#daida de dados
print("a media da diciplina é:", media)