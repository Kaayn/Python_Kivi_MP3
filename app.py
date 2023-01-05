import tkinter as tk
import speech_recognition as sr
from tkinter import filedialog

# Création de la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Mon interface")

# Fonction de reconnaissance de parole


def reconnaissance_parole(fichier_audio):
    # Chargement du fichier audio
    r = sr.Recognizer()
    with sr.AudioFile(fichier_audio) as source:
        audio = r.record(source)

    # Reconnaissance de la parole
    try:
        texte = r.recognize_google(audio, language="fr-FR")
        print(texte)

        # Enregistrement du résultat dans un fichier
        with open("resultat.txt", "w") as fichier:
            fichier.write(texte)
    except sr.UnknownValueError:
        print("La parole n'a pas pu être reconnue")

# Création du sélecteur de fichier


def ouvrir_fichier():
    fichier = filedialog.askopenfilename(
        title="Sélectionner un fichier audio", filetypes=[("Fichiers audio", "*.wav")])
    reconnaissance_parole(fichier)


# Création du bouton pour ouvrir le sélecteur de fichier
btn_fichier = tk.Button(
    fenetre, text="Sélectionner un fichier audio", command=ouvrir_fichier)
btn_fichier.pack()

# Affichage de la fenêtre
fenetre.mainloop()
