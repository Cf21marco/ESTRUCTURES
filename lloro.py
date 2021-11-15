#!/bin/python3
#_*_ coding: utf-8 _*_
"""
  lloro.py
  aquest codi repeteix la frase entrada per l'usuari indefinidament fins que s'entri una frase buida (i.e. un enter)

  nota: la funció isinstance(var,str) retorna True si 'var' és un string i False si no ho és.
"""

__author__ = "Marco Flores"

if __name__ == '__main__':
  is_empty = False
  while is_empty == False:
    sentence = input("L'usuari diu: ")
    if isinstance(sentence, str) == False:
      print("Aquest input és erroni. Afegim un exemple d'ús:")
      print(" $ python3 lloro.py")
      print("L'usuari diu: <frase escrita per l'usuari 1>")
      print("El lloro repeteix: <frase escrita per l'usuari 1>")
      print("L'usuari diu: <frase escrita per l'usuari 2>")
      print("El lloro repeteix: <frase escrita per l'usuari 2>")
      print("...")
      print("\n")
      quit()
    elif len(sentence)==0:
      is_empty = True 
    else:
      print('El lloro repeteix: ',sentence)
      