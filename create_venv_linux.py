import subprocess

pfad = input("Bitte gebe den Pfad ein das Python VENV erstellt werden soll: ")
projekt = input("Welchen Name hat das Projekt? ")
print("Warte einen Moment...")

# Create the VENV with pip
subprocess.run(["sudo", "/usr/bin/python3", "-m", "venv", f"{pfad}/{projekt}"])

print("Dein Python VENV wurde erstellt.")
print("Druecke Enter zum beenden.")
input()