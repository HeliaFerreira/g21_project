# -*- coding: utf-8 -*-
"""
Created on Mon May 18 23:48:26 2026

@author: marti
"""
#creates a curator 

c1 = Curator(2001, "Curador Principal Teste", 501, 1) 
c2 = Curator.from_string("2002;Curador Assistente Teste;502;2")

if c1.id not in Curator.lst:
    Curator.insert(c1.id)
if c2.id not in Curator.lst:
    Curator.insert(c2.id)

print(Curator.obj[2001])
print(Curator.obj[2002])

#creates 2 visitors 
v1 = Visitors(9001, 1001, 501, "2025-12-31", 500)
v2 = Visitors.from_string("9002;1002;502;2025-12-31;850")

if v1.id not in Visitors.lst:
    Visitors.insert(v1.id)
if v2.id not in Visitors.lst:
    Visitors.insert(v2.id)

print(Visitors.obj[9001])
print(Visitors.obj[9002])