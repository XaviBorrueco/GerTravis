#Thats a putisima idisima de holla

import random
import os
import sys
import time
import pyautogui

version = 0.1
os.system('color 0d')
os.system("cls")
menu = """
************************
		WELCOME
************************
[Juego]
[Trabajo]
[Ideas]
"""

def sistema(): 
	peticion = input("¿Que quieres aser? ")
	peticion = peticion.lower()
	if peticion.find("juegos") != -1 or peticion.find("jugar") != -1:
		juegos()
	if peticion.find("programar") != -1 or peticion.find("trabajar") != -1 or peticion.find("python") != -1 or peticion.find("trabajo") != -1:
		trabajar()
	if peticion.find("idea") != -1 or peticion.find("ideas") != -1:
		ideas()
	if peticion.find("dioso") != -1 or peticion.find("exit") != -1 or peticion.find("salir") != -1:
		print("Diosoooo bb")
		exit()

def juegos():
	game = input("¿Que juego quieres jugar? ")
	game = game.lower()
	if game.find("overwatch") != -1:
		os.system(r"C:\Users\borru\Desktop\Gertravis\Juegos\Overwatch.lnk")
	elif game.find("steam") != -1:
		print("comprate el disco de el juego en fisico k no lo puedo abrir XD  ")
	elif game.find("csgo") != -1 or game.find("counter") != -1:
		print("comprate el disco de el juego en fisico k no lo puedo abrir XD  ")
	elif game.find("pubg") != -1 or game.find("player") != -1:
		print("comprate el disco de el juego en fisico k no lo puedo abrir XD  ")
	elif game.find("sniper") != -1 or game.find("ghost") != -1 or game.find("warrior") != -1:
		print("comprate el disco de el juego en fisico k no lo puedo abrir XD ")
	else:
		print("No he encontrado el juego en la base de datos, compratelo puto pobre de mierda PD: Fake bitch")

#Carala guapa.
def trabajar():
	work = input("¿Que quieres abrir? ")
	work = work.lower()
	if work.find("sublime") != -1:
		os.system("sublime_text")

	if work.find("google") != -1 or work.find("chrome") != -1:
		go = input("¿Quieres entrar en alguna pagina en concreto? ")
		if go == "si" or go == "s" :
			ww = input("¿Cual?: ")
			os.system("start chrome.exe " + ww + ".com")
		else:
			os.system("start chrome.exe www.google.com")

def ideas():
	nideas = 0
	idea = input("Tienes una idea ")
	if idea != "si":
		db = open("db.txt", "r")
		print("Estas son tus ideas: ")
		for i in db:
			#numero de ideasssssssss
			nideas += 1
		db.close()
		db = open("db.txt", "r")

		ide = db.readlines()
		for i in range(0,nideas):
			print(ide[i])

	else:
		db = open("db.txt", "a")
		carla = input("¿Cual es tu idea amorr? ")
		print("Excelente idea guapo, la guardare en el fondo de mi corazon(en db.txt)")
		db.write(carla + "\n")	
while True:
	print(menu)
	sistema()	