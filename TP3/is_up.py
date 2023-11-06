import os
import sys

ping_command = f"ping {sys.argv[1]}"

# Exécute la commande ping et capture la sortie dans une variable
ping_output = os.popen(ping_command).read()

# Vérifie si le résultat du ping contient "TTL=" (utilisé pour déterminer si le ping a réussi)
if "TTL=" in ping_output:
  print("UP !")
else:
  print("DOWN !")
