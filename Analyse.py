import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ==============================
# 1. Chargement du dataset
# ==============================

# ⚠️ عدّلي الاسم إلا كان مختلف
df = pd.read_csv("student_data (1).csv")

print("===== APERÇU DU DATASET =====")
print(df.head())

# ==============================
# 2. Informations générales
# ==============================
print("\n===== INFORMATIONS GÉNÉRALES =====")
print(df.info())

print("\n===== STATISTIQUES DESCRIPTIVES =====")
print(df.describe())

# ==============================
# 3. Valeurs manquantes
# ==============================
print("\n===== VALEURS MANQUANTES =====")
print(df.isnull().sum())

# ==============================
# 4. Feature Engineering
# ==============================

# Resultat (Réussi / Échoué) basé على G3 (note finale)
df["result"] = df["G3"].apply(lambda x: "Réussi" if x >= 10 else "Échoué")

# Mention académique
def mention(note):
    if note >= 16:
        return "Très Bien"
    elif note >= 14:
        return "Bien"
    elif note >= 12:
        return "Assez Bien"
    elif note >= 10:
        return "Passable"
    else:
        return "Insuffisant"

df["mention"] = df["G3"].apply(mention)

# Moyenne générale par étudiant
df["average"] = (df["G1"] + df["G2"] + df["G3"]) / 3

print("\n===== DATASET APRÈS TRANSFORMATION =====")
print(df[["G1", "G2", "G3", "average", "result", "mention"]].head())

# ==============================
# 5. Analyse globale
# ==============================
moyenne_generale = df["G3"].mean()
taux_reussite = (df["result"] == "Réussi").mean() * 100

print("\n===== ANALYSE GLOBALE =====")
print("Moyenne générale (G3) :", round(moyenne_generale, 2))
print("Taux de réussite :", round(taux_reussite, 2), "%")

# ==============================
# 6. Analyse par sexe
# ==============================
print("\n===== MOYENNE PAR SEXE =====")
print(df.groupby("sex")["G3"].mean())

plt.figure()
sns.boxplot(x="sex", y="G3", data=df)
plt.title("Distribution des notes finales (G3) selon le sexe")
plt.xlabel("Sexe")
plt.ylabel("Note finale (G3)")
plt.show()

# ==============================
# 7. Analyse par école
# ==============================
print("\n===== MOYENNE PAR ÉCOLE =====")
print(df.groupby("school")["G3"].mean())

plt.figure()
sns.barplot(x="school", y="G3", data=df)
plt.title("Moyenne des notes finales (G3) par école")
plt.xlabel("École")
plt.ylabel("Note finale moyenne")
plt.show()

# ==============================
# 8. Relation âge / performance
# ==============================
plt.figure()
sns.scatterplot(x="age", y="G3", hue="result", data=df)
plt.title("Relation entre l'âge et la note finale (G3)")
plt.xlabel("Âge")
plt.ylabel("Note finale (G3)")
plt.show()

# ==============================
# 9. Répartition des mentions
# ==============================
plt.figure()
df["mention"].value_counts().plot(kind="pie", autopct="%1.1f%%", startangle=90)
plt.title("Répartition des mentions académiques")
plt.ylabel("")
plt.show()

# ==============================
# 10. Conclusions
# ==============================
print("\n===== CONCLUSIONS =====")
print("- La majorité des étudiants ont validé l'année.")
print("- Les performances varient selon le sexe et l'école.")
print("- La note finale G3 est un bon indicateur de réussite.")
