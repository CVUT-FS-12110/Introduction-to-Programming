import os
import time
from pathlib import Path

NUMBER_OF_LINES = 10
DEFAULT_FILE = "data1.txt"


filepath = input(f"Jaký soubor se má otevřít (defaultně to bude {DEFAULT_FILE})? ")
if not filepath:
   filepath = DEFAULT_FILE

filepath = Path(filepath)

try:
   with open(filepath, "r", encoding="utf-8") as file:
       content = file.read()
   print("Soubor nalezen.")
except FileNotFoundError:
   filepath.parent.mkdir(parents=True, exist_ok=True)
   with open(filepath, "w", encoding="utf-8") as file:
       pass
   print("Soubor nenalezen. Soubor byl vytvořen.")
  
time.sleep(1)
print("Úspěch soubor otevřen.")
time.sleep(1)


while True:
   os.system("clear")
   print(f"Super Editor: {filepath}")
   with open(filepath, "r", encoding="utf-8") as file:
       content = file.read()
  
   clean_lines = []
   for idx, line in enumerate(content.split("\n"), start=1):
       if line:
           clean_lines.append(f"{str(idx).rjust(5)}:  {line}")

   for clean_line in clean_lines[-NUMBER_OF_LINES:]:
       print(clean_line)

   new_line = input("Přidejte nový řádek nebo napište příkaz: ")
   if new_line.startswith("\\"):
       if new_line == "\\exit":
           print("Program byl ukončen uživatelem.")
           break
       elif new_line == "\\clear":
           with open(filepath, "w", encoding="utf-8") as file:
               file.write("")
   else:
       with open(filepath, "a", encoding="utf-8") as file:
           file.write(f"{new_line}\n")