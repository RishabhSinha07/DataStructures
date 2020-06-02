def kinetic_energy(m:'in KG', v:'in M/S')->'Joules':
    return 1/2*m*v**2

print(kinetic_energy(2,3),end="")
print(kinetic_energy.__annotations__['return'])