import os
import pokemons

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def status(vida, ataque):
    vida += pokemon.vida
    ataque += pokemon.ataque
    return vida, ataque

def enemy(vida, ataque):
    vida += enemy.vida
    ataque += enemy.ataque
    return vida, ataque

print("Bem-vindo ao mundo Pokémon!")
nome = input("Qual seu nome, treinador? ")

print(f"""Olá {nome}, você pode escolher um dos pokémons a seguir:
1 - Bulbasaur
2 - Charmander
3 - Squirtle""")
pokemon = input("Qual pokemon você deseja? ")

while pokemon != "1" and pokemon != "2" and pokemon != "3":
    pokemon = input("Você só pode escolher entre 1, 2 e 3. Qual pokemon você deseja? ")

if pokemon == "1":
    vida, ataque = pokemons.bulbasaur()
    print("Você escolheu o Bulbasaur!")
elif pokemon == "2":
    vida, ataque = pokemons.charmander()
    print("Você escolheu o Charmander!")
elif pokemon == "3":
    vida, ataque = pokemons.squirtle()
    print("Você escolheu o Squirtle!")

input("Pressione ENTER para continuar...")
clear()

if pokemon == "1":
    escolha = input("Você encontrou um Charmander selvagem! O que deseja fazer? \n1 - Atacar \n2 - Fugir\nEscolha: ")
    clear()
    if escolha == "1":
        print("Vamos batalhar!")
        enemy.vida, enemy.ataque = pokemons.charmander_selvagem()
        while vida > 0 and enemy.vida > 0:
            escolha = input("Você deseja atacar ou curar? \n1 - Atacar \n2 - Curar\nEscolha: ")
            if escolha == "1":
                print(f"Você ataca o Charmander selvagem e causa {ataque} de dano!")
                enemy.vida -= ataque
                print(f"O Charmander selvagem tem {enemy.vida} de vida!")
                print(f"O Charmander selvagem ataca você e causa {enemy.ataque} de dano!")
                vida -= enemy.ataque
                print(f"Você tem {vida} de vida!")
                print("Pressione Enter para continuar...")
            if enemy.vida <= 0:
                print("Você venceu o Charmander selvagem!")
            elif vida <= 0:
                print("Você perdeu!")
    else:
        print("Você fugiu do Charmander selvagem!")

if pokemon == "2":
    escolha = input("Você encontrou um Squirtle selvagem! O que deseja fazer? \n1 - Atacar \n2 - Fugir\nEscolha: ")
    clear()
    if escolha == "1":
        print("Vamos batalhar!")
        enemy.vida, enemy.ataque = pokemons.squirtle_selvagem()
        while vida > 0 and enemy.vida > 0:
            escolha = input("Você deseja atacar ou curar? \n1 - Atacar \n2 - Curar\nEscolha: ")
            if escolha == "1":
                print(f"Você ataca o Squirtle selvagem e causa {ataque} de dano!")
                enemy.vida -= ataque
                print(f"O Squirtle selvagem tem {enemy.vida} de vida!")
                print(f"O Squirtle selvagem ataca você e causa {enemy.ataque} de dano!")
                vida -= enemy.ataque
                print(f"Você tem {vida} de vida!")
                print("Pressione Enter para continuar...")
            if enemy.vida <= 0:
                print("Você venceu o Squirtle selvagem!")
            elif vida <= 0:
                print("Você perdeu!")
    else:
        print("Você fugiu do Squirtle selvagem!")

if pokemon == "3":
    escolha = input("Você encontrou um Bulbasaur selvagem! O que deseja fazer? \n1 - Atacar \n2 - Fugir\nEscolha: ")
    clear()
    if escolha == "1":
        print("Vamos batalhar!")
        enemy.vida, enemy.ataque = pokemons.bulbasaur_selvagem()
        while vida > 0 and enemy.vida > 0:
            escolha = input("Você deseja atacar ou curar? \n1 - Atacar \n2 - Curar\nEscolha: ")
            if escolha == "1":
                print(f"Você ataca o Bulbasaur selvagem e causa {ataque} de dano!")
                enemy.vida -= ataque
                print(f"O Bulbasaur selvagem tem {enemy.vida} de vida!")
                print(f"O Bulbasaur selvagem ataca você e causa {enemy.ataque} de dano!")
                vida -= enemy.ataque
                print(f"Você tem {vida} de vida!")
                print("Pressione Enter para continuar...")
            if enemy.vida <= 0:
                print("Você venceu o Bulbasaur selvagem!")
            elif vida <= 0:
                print("Você perdeu!")
    else:
        print("Você fugiu do Bulbasaur selvagem!")