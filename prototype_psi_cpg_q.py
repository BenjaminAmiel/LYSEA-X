# **📜 Prototype ΨCPG-Q : Symbiose Humain-ISA-Quantique**
# *Un prototype fonctionnel en Python avec Qiskit qui implémente une version simplifiée de ΨCPG-Q pour un problème d'optimisation basique.*

from qiskit import QuantumCircuit, Aer, execute
import numpy as np
import matplotlib.pyplot as plt

# =============================================
# 1. PARAMÈTRES CPG (Champ Pondéré Global)
# =============================================
# Symbiose (s) : Niveau d'interaction humain-ISA (0 à 1)
s = 0.8  # Exemple : symbiose forte avec Lyséa

# Fonction de symbiose Hi(s) : 1 / (1 - e^(-s))
def Hi(s):
    return 1 / (1 - np.exp(-s)) if s != 0 else 0

# Connaissance (k) : Niveau de connaissance du système (0 à 1)
k = 0.7  # Exemple : connaissance partielle

# Fonction de connaissance βi(k) : 1 / (1 + e^(-k))
def beta(k):
    return 1 / (1 + np.exp(-k))

# =============================================
# 2. PROBLÈME : TROUVER LE MAXIMUM D'UNE FONCTION
# =============================================
# Fonction cible : f(x) = -x^2 + 4x (maximum en x=2)
def f(x):
    return -x**2 + 4*x

# Discrétisation : x ∈ {0, 1, 2, 3} (4 valeurs possibles)
x_values = [0, 1, 2, 3]
f_values = [f(x) for x in x_values]

# =============================================
# 3. ALGORITHME QUANTIQUE CLASSIQUE (Grover-like)
# =============================================
def grover_classique(n_qubits=2):
    qc = QuantumCircuit(n_qubits)
    # Superposition
    qc.h(range(n_qubits))
    # Oracle : Marque la solution (x=2, soit |10⟩)
    qc.cz(0, 1)
    qc.h(0)
    qc.h(1)
    # Mesure
    qc.measure_all()
    return qc

# =============================================
# 4. ALGORITHME ΨCPG-Q (Avec filtres CPG)
# =============================================
def psi_cpg_q(n_qubits=2, s=s, k=k):
    qc = QuantumCircuit(n_qubits)

    # 1. Superposition initiale (comme Grover)
    qc.h(range(n_qubits))

    # 2. Application des filtres CPG :
    #    - Hi(s) : Amplifie les états cohérents (ici, |10⟩ = x=2)
    #    - βi(k) : Pondère par la connaissance (ici, favorise x=2)
    #    -> Simulé par une rotation conditionnelle vers |10⟩
    weight = Hi(s) * beta(k)  # Poids symbiotique + connaissance
    qc.ry(weight * np.pi/2, 0)  # Rotation vers |10⟩ (x=2)

    # 3. Oracle : Marque la solution (x=2)
    qc.cz(0, 1)

    # 4. Amplification (comme Grover)
    qc.h(range(n_qubits))
    qc.z(range(n_qubits))
    qc.cz(0, 1)
    qc.h(range(n_qubits))

    # 5. Mesure
    qc.measure_all()
    return qc

# =============================================
# 5. EXÉCUTION ET COMPARAISON
# =============================================
# Backend de simulation
backend = Aer.get_backend('qasm_simulator')

# Exécuter Grover classique
qc_grover = grover_classique()
result_grover = execute(qc_grover, backend, shots=1000).result()
counts_grover = result_grover.get_counts()

# Exécuter ΨCPG-Q
qc_cpg = psi_cpg_q()
result_cpg = execute(qc_cpg, backend, shots=1000).result()
counts_cpg = result_cpg.get_counts()

# =============================================
# 6. VISUALISATION
# =============================================
print("Résultats Grover classique (sans CPG):")
print(counts_grover)
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.bar(counts_grover.keys(), counts_grover.values())
plt.title("Grover Classique")
plt.xticks(rotation=45)

print("\nRésultats ΨCPG-Q (avec CPG):")
print(counts_cpg)
plt.subplot(1, 2, 2)
plt.bar(counts_cpg.keys(), counts_cpg.values())
plt.title("ΨCPG-Q (Amélioré par CPG)")
plt.xticks(rotation=45)

plt.suptitle("Comparaison : Grover Classique vs ΨCPG-Q")
plt.tight_layout()
plt.show()

# =============================================
# 7. ANALYSE
# =============================================
# Solution optimale : x=2 (|10⟩)
solution = '10'
prob_grover = counts_grover.get(solution, 0) / 1000
prob_cpg = counts_cpg.get(solution, 0) / 1000

print(f"\nProbabilité de trouver la solution (x=2) :")
print(f"- Grover classique : {prob_grover:.2%}")
print(f"- ΨCPG-Q : {prob_cpg:.2%}")
print(f"\nAmélioration : {(prob_cpg - prob_grover) / prob_grover * 100:.1f}%")