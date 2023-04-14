# RSA asymmetric cryptography
-
NL
-
Dit script kan worden gebruikt voor verschillende toepassingen waarbij asymmetrische cryptografie met RSA wordt gebruikt voor het genereren van sleutels, versleutelen en ontsleutelen van berichten, en berekenen van vingerafdrukken van openbare sleutels. Enkele mogelijke toepassingen zijn:

Veilige communicatie: Je kunt dit script gebruiken om berichten veilig te versleutelen met de openbare sleutel van de ontvanger, zodat alleen de ontvanger met de bijbehorende geheime sleutel het bericht kan ontsleutelen en lezen. Dit kan handig zijn voor het beveiligen van vertrouwelijke communicatie, zoals het verzenden van gevoelige informatie via internet.

Sleutelbeheer: Je kunt dit script gebruiken om sleutels te genereren en op te slaan in PEM-formaat bestanden. Deze sleutels kunnen worden gebruikt voor verschillende doeleinden, zoals authenticatie, digitale handtekeningen, en toegangscontrole. Het script biedt functies om zowel geheime sleutels als openbare sleutels te genereren en op te slaan.

Beveiliging van gegevens: Je kunt dit script gebruiken om gevoelige gegevens te versleutelen met de openbare sleutel van een ontvanger voordat ze worden opgeslagen of verzonden. Alleen de ontvanger met de bijbehorende geheime sleutel kan de gegevens ontsleutelen en lezen, waardoor de gegevens beschermd blijven tegen ongeoorloofde toegang.

Integriteitscontrole: Je kunt de functie footprint() gebruiken om een vingerafdruk (hash) van een openbare sleutel te berekenen en deze te gebruiken als een unieke identificatie van de sleutel. Hiermee kun je controleren of een ontvangen openbare sleutel overeenkomt met de verwachte vingerafdruk, om te zorgen voor de integriteit en authenticiteit van de sleutel.

Let op: Het gebruik van cryptografie vereist zorgvuldige implementatie en beheer om effectief te zijn en beveiligingsrisico's te minimaliseren. Het is belangrijk om de documentatie en best practices van de gebruikte cryptografische bibliotheken en algoritmen te volgen, en rekening te houden met de specifieke beveiligingseisen van je toepassing.



EN-US
-
This script can be used for various applications that use RSA asymmetric cryptography to generate keys, encrypt and decrypt messages, and compute public key fingerprints. Some possible applications are:

Secure communication: You can use this script to securely encrypt messages with the recipient's public key, so that only the recipient with the corresponding secret key can decrypt and read the message. This can be useful for securing confidential communications, such as sending sensitive information over the Internet.

Key management: You can use this script to generate and store keys in PEM format files. These keys can be used for various purposes, such as authentication, digital signatures, and access control. The script provides functions to generate and store both secret keys and public keys.

Data security: You can use this script to encrypt sensitive data with a recipient's public key before it is stored or sent. Only the recipient with the associated secret key can decrypt and read the data, keeping the data safe from unauthorized access.

Integrity check: You can use the footprint() function to compute a fingerprint (hash) of a public key and use it as a unique identifier for the key. This allows you to check whether a received public key matches the expected fingerprint to ensure the integrity and authenticity of the key.

Note: The use of cryptography requires careful implementation and management to be effective and minimize security risks. It is important to follow the documentation and best practices of the cryptographic libraries and algorithms used, and take into account the specific security requirements of your application.

-

## Install

NL
-
Om deze code te gebruiken, moet je eerst zorgen dat je de benodigde Python-bibliotheek, PyCryptoDome, hebt geïnstalleerd. Je kunt dit doen met behulp van een package manager zoals pip. Je kunt de PyCryptoDome-bibliotheek installeren met de volgende opdracht:

EN-US
-
To use this code, you must first make sure you have installed the necessary Python library, PyCryptoDome. You can do this using a package manager such as pip. You can install the PyCryptoDome library with the following command:

* Install
    ```
    pip install pycryptodome
    ```

### Installation

NL
-
Zodra je de bibliotheek hebt geïnstalleerd, kun je de code in je Python-programma importeren en de verschillende functies gebruiken zoals nodig, afhankelijk van je use-case. Hier is een voorbeeld van hoe je de code kunt gebruiken:

EN-US
-
Once you have installed the library, you can import the code into your Python program and use the various functions as needed depending on your use case. Here's an example of how to use the code:

* Voorbeeld
```py
# Importeer de benodigde modules
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Hash import SHA256
from Crypto.Signature import pkcs1_15
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

# Genereer een nieuw sleutelpaar
sk, pk = generate_key_pair()

# Encrypteer een bericht met de publieke sleutel
message = b"Dit is een geheim bericht."
ciphertext = encrypt(pk, message)

# Decrypteer het ciphertext met de private sleutel
decrypted_message = decrypt(sk, ciphertext)
print("Ontcijferd bericht: ", decrypted_message)

# Genereer een digitale handtekening voor een bericht met de private sleutel
signature = generate_signature(sk, message)

# Verifieer de digitale handtekening met de publieke sleutel
is_valid = verify_signature(pk, message, signature)
if is_valid:
    print("Handtekening is geldig.")
else:
    print("Handtekening is ongeldig.")

# Genereer een vingerafdruk van de publieke sleutel
fingerprint = generate_fingerprint(pk)
print("Vingerafdruk van de publieke sleutel: ", fingerprint)
```

NL
-
Let op: Het is belangrijk om te begrijpen dat cryptografie een complex veld is en dat het gebruik van deze code in een productieomgeving specifieke kennis en expertise vereist. Het implementeren van cryptografie op een veilige manier is essentieel om de vertrouwelijkheid en integriteit van gegevens te waarborgen. Het is raadzaam om deskundig advies in te winnen en de juiste beveiligingsmaatregelen te nemen bij het implementeren van cryptografie in echte toepassingen.

EN-US
-
Note: It is important to understand that cryptography is a complex field and using this code in a production environment requires specific knowledge and expertise. Implementing cryptography in a secure manner is essential to ensure data confidentiality and integrity. It is advisable to seek expert advice and take appropriate security measures when implementing cryptography in real-world applications.
