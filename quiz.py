print("----The BigBang Theory----")
print("Bem vindo ao quiz!")
resposta_usuario = input("Vamos começar? (S/N)")

if resposta_usuario != "S":
    quit()

score = 0

print("Começando...")
print("1-Qual é a origem do termo Bazinga?\n (A)  Sheldon inventou \n (B) Veio de um programa infantil \n (C) É a forma que sheldon usa pra indicar sarcasmo \n (D) Bordão do Leonard \n")
resposta_1 = input("Resposta: ")

if resposta_1 == "C":
    print("Correto!")
    score = score + 1
else:
    print("Incorreto!")


print("2-Qual foi o nome do primeiro namorado da Penny?\n (A) Mike \n (B) Doug \n (C)Kurt \n (D) Zack \n")
resposta_2 = input("Resposta: ")

if resposta_2 == "C":
    print("Correto!")
    score = score + 1
else:
    print("Incorreto!")


print("3-Em qual universidade os personagens principais trabalham?\n (A) MIT \n (B) Caltech \n (C) Stanford \n (D) Ucla \n")
resposta_3 = input("Resposta: ")

if resposta_3 == "B":
    print("Correto!")
    score = score + 1
else:
    print("Incorreto!")


print("4-Em que cidade se passa a série\n (A) San Francisco \n (B) Pasadena \n (C) Boston \n (D) Austin \n")
resposta_4 = input("Resposta: ")

if resposta_4 == "B":
    print("Correto!")
    score = score + 1
else:
    print("Incorreto!")


print("5-Qual desses personagens NÃO possui doutorado\n (A) Raj \n (B) Leonard \n (C) Sheldon \n (D) Howard \n")
resposta_5 = input("Resposta: ")

if resposta_5 == "D":
    print("Correto!")
    score = score + 1
else:
    print("Incorreto!")

print(f"Obrigada por participar! Sua pontuação foi: {score}/5")

