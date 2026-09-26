import pandas as pd
import matplotlib.pyplot as plt

# Lire le fichier CSV
data = pd.read_csv(
    "dataset_croissance_maroc.csv",
    sep=";",
    encoding="latin1"
)

# Afficher les données
print(data)

# Créer le graphique
plt.figure(figsize=(10, 6))

plt.plot(
    data["Année"],
    data["Croissance du PIB (%)"].str.replace(",", ".").astype(float),
    marker="o",
    label="Croissance du PIB"
)

plt.plot(
    data["Année"],
    data["Taux de chômage (%)"].str.replace(",", ".").astype(float),
    marker="o",
    label="Taux de chômage"
)

plt.title("Évolution de la croissance économique et du chômage au Maroc")
plt.xlabel("Année")
plt.ylabel("Pourcentage (%)")

plt.legend()
plt.grid(True)

# Enregistrer le graphique
plt.savefig("graphique_croissance_chomage.png")

# Afficher le graphique
plt.show()
