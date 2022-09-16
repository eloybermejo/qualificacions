# Eloy Bermejo i Nico Diaz
# Definició de classes
# Definició de classes
class UnitatFormativa:
    nom = None
    qualificacio = None

    def __init__(self, nom):
        self.nom = nom


# Inici del programa
uf1 = UnitatFormativa("UF1. Desenvolupament del programari")
uf2 = UnitatFormativa("UF2. Optimització del programari")
uf3 = UnitatFormativa("UF3. Introducció al Disseny Orientat a Objectes")

uf1.qualificacio = 8
uf2.qualificacio = 10
uf3.qualificacio = 4

print(uf1.nom, ":", uf1.qualificacio)
print(uf2.nom, ":", uf1.qualificacio)
print(uf3.nom, ":", uf1.qualificacio)