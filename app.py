import tkinter as tk
import speech_recognition as sr
from tkinter import filedialog
from pydub import AudioSegment
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
import base64

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
            texte = r.recognize_google(audio, language="FR-fr")
            print(texte)

            # Enregistrement du résultat dans un fichier
            with open("resultat.txt", "w") as fichier:
                fichier.write(texte)
                texteCrypte = texte
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

# Creation du cryptage du texte
# pip install cryptography
# génération de la clé privée
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
    backend=default_backend()
)
# génération de la clé publique à partir de la privée
public_key = private_key.public_key()
# genere le fichier de clé privée
pem = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.PKCS8,
    encryption_algorithm=serialization.NoEncryption()
)
with open('private_key.pem', 'wb') as f:
    f.write(pem)
# génére le fichier de clé publique
pem = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)
with open('public_key.pem', 'wb') as f:
    f.write(pem)


with open("public_key.pem", "rb") as key_file:
    public_key = serialization.load_pem_public_key(
        key_file.read(),
        backend=default_backend()
    )
message = input("Message chiffré: ")


encrypted = public_key.encrypt(
    bytes(message, 'utf-8'),
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)
message_chiffre = base64.b64encode(encrypted)
print("Message chiffré: ", message_chiffre)

with open("private_key.pem", "rb") as key_file:
    private_key = serialization.load_pem_private_key(
        key_file.read(),
        password=None,
        backend=default_backend()
    )
message = input("Message à décrypter: ")
message_decode = base64.b64decode(message)
original_message = private_key.decrypt(
    message_decode,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)
print("Message déchiffré: ", original_message.decode('UTF-8'))


# Affichage de la fenêtre
fenetre.mainloop()