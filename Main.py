from Organism import *
from CPU import CPU
from LocMem import CPUMem
import random

ances_code = open("80aaa.txt", "wb")
Soup = G_Memory()
OS = operating_system(Soup)
ances_CPU = CPU(Soup)
ances_name = "origin"
ances_mem = CPUMem()
ancestor = Organism(ances_code, ances_CPU, ances_name)

if ances_mem.total_moved > random.random() * (2500 - 1000) + 1000:
    OS.mutation()