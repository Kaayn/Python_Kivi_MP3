import uuid
import hashlib
import random
import string

texte = "caca"
salt = uuid.uuid4().hex

def hash_texte(texte):
    
    hashedTexte = hashlib.sha256(salt.encode() + texte.encode()).hexdigest() + ':' + salt
    return print(hashedTexte)

def unhash_texte(hashedTexte):
   
    hashedTexte, salt = hashedTexte.split(':')
    texteUncrypt = hashlib.sha256(salt.encode() + texteUncrypt.encode()).hexdigest()
    return print(texteUncrypt)

hash_texte(texte)
unhash_texte(hash_texte(texte))
#characters = string.ascii_letters + string.digits + string.punctuation
#texte = ''.join(random.choice(characters) for i in range(8))