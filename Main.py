from CPU import CPU
from OS import operating_system
from Memory import G_Memory
import random

Global = G_Memory()
OS = operating_system(Global)
ances_CPU = CPU(OS)
i = 0
with open('80aaa.txt', 'r') as ancestor:
    for line in ancestor:
        Global.RAM[i] = line
        i += 1
ances_CPU.mem.length = i - 1
ances_CPU.mem.end = i - 1
ances_CPU.mem.name(Global.names)
for j in range(0, i - 1):
    Global.property[i] = ances_CPU.mem.name
Global.accessory[ances_CPU.mem.name] = ances_CPU
Global.cells_alive += 1
OS.slicer_start(ances_CPU)
ances_CPU.run()


