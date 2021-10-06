# Program za izračun ploščine kroga

# Vključitev zahtevanih Python knjižnic
import math

# Vnos podatkov
radij = float(input("Podaj radij kroga: "))

# Izračun iskanih vrednosti
ploscina = math.pi * radij**2

# Izpis izračunanih vrednosti 
print(f"Ploščina kroga je {ploscina:.3f}")
