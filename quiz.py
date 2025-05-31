print("----The BigBang Theory----")
print("Bem vindo ao quiz!")
answer_user = input("Vamos começar? (S/N)")

if answer_user != "S":
    quit()

score = 0

print("Começando...")
print("1-Qual é a origem do termo Bazinga?\n (A)  Sheldon inventou \n (B) Veio de um programa infantil \n (C) É a forma que sheldon usa pra indicar sarcasmo \n (D) Bordão do Leonard \n")
answer_1 = input("Resposta: ")

if answer_1 == "C":
    print("Correto!")
    score = score + 1
else:
    print("Incorreto!")


print("2-Qual foi o nome do primeiro namorado da Penny?\n (A) Mike \n (B) Doug \n (C)Kurt \n (D) Zack \n")
answer_1 = input("Resposta: ")

if answer_1 == "C":
    print("Correto!")
    score = score + 1
else:
    print("Incorreto!")


print("3-Em qual universidade os personagens principais trabalham?\n (A) MIT \n (B) Caltech \n (C) Stanford \n (D) Ucla \n")
answer_1 = input("Resposta: ")

if answer_1 == "B":
    print("Correto!")
    score = score + 1
else:
    print("Incorreto!")


print("4-Em que cidade se passa a série\n (A) San Francisco \n (B) Pasadena \n (C) Boston \n (D) Austin \n")
answer_1 = input("Resposta: ")

if answer_1 == "B":
    print("Correto!")
    score = score + 1
else:
    print("Incorreto!")


print("5-Qual desses personagens NÃO possui doutorado\n (A) Raj \n (B) Leonard \n (C) Sheldon \n (D) Howard \n")
answer_1 = input("Resposta: ")

if answer_1 == "D":
    print("Correto!")
    score = score + 1
else:
    print("Incorreto!")

print(f"Obrigada por participar! Sua pontuação foi: {score}/5")

