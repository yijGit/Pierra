from CPU import CPU

from OS import operating_system
from Memory import G_Memory
import random

Global = G_Memory
OS = operating_system(Global)
ances_CPU = CPU(OS)
i = 0
with open('80aaa.txt', 'r') as ancestor:
    for line in ancestor:
        G_Memory.RAM[i] = line
        i += 1
ances_CPU.mem.length = i - 1
ances_CPU.mem.end = i - 1


