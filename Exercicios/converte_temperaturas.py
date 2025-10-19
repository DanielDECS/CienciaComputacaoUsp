# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 00:44:40 2020

@author: Danie
"""

def converte_temperaturas(tf):
    tc = (tf - 32) / 9 * 5
    return(tc)

a = int(input("Informe a temperatura em Farenheit: "))
print("A temperatura em Celsius equivalente é: ", converte_temperaturas(a))