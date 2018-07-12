from OS import *
from Memory import *
from Organism import *
from vm import *

ances_code = open("80aaa.txt", "wb")
Soup = G_Memory()
OS = operating_system(Soup)
ances_CPU = Machine()
ances_name = "origin"
ancestor = Organism(ances_code, ances_CPU, Soup, OS, ances_name)

