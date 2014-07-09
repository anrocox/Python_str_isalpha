#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on Jul 9, 2014

@author: anroco

How to know if the characters in a python str are alphabetic?

¿Como saber si los caracteres de un str python son letras?
'''

#create a str
s = 'programming'
print(s)

#verify if all characters in the string are alphabetic. Are those defined in
#Unicode as “Letter”. Return True or False
print(s.isalpha())

#create a str
s = 'programming in python'
print(s)

#return False because exists space characters
print(s.isalpha())
