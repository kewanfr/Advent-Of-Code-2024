# Simple script to download input files from Advent of Code
# Don't forget to put your session token in session.txt
# You can find it in your browser cookies
# This script will create a folder for each day, and put the input file in it

import os, sys
import requests
from datetime import datetime

YEAR_IN_FOLDER_NAME = False # If True, the folder will be named "2020 Dec" instead of "Dec"
current_year = datetime.now().year # Change this if you want to download input files from another year
current_day = datetime.now().day

if not os.path.exists(os.path.dirname(os.path.realpath(__file__)) + "/session.txt"):
  print("Error: session.txt not found")
  sys.exit(1)

os.environ["AOC_SESSION"] = open(os.path.dirname(os.path.realpath(__file__)) + "/session.txt", "r").read()


def download_input_txt_file(day, year, year_in_folder_name = False):
  file_dir = os.path.dirname(os.path.realpath(__file__))
  if year_in_folder_name:
    file_dir = os.path.join(file_dir, str(year) + " ")
  
  file_dir = os.path.join(file_dir, "Dec " + str(day))

  os.makedirs(os.path.dirname(file_dir), exist_ok=True)
  file_path = os.path.join(file_dir, "input.txt")

  request = requests.get("https://adventofcode.com/" + str(year) + "/day/" + str(day) + "/input", cookies={"session": os.environ["AOC_SESSION"]})
  
  if request.status_code == 200:
    file_input = request.text
    open(file_path, "w").write(file_input)
    print("Fichier d'input du jour récupéré avec succès !")
  else:
    print("Error: " + str(request.status_code))
    print("X Impossible de récupérer le fichier d'entrée. Il est possible que le jour ne soit pas encore sorti, ou que le token de session.txt soit invalide.")

  
if __name__ == "__main__":
  print("Downloading input file for", current_year, "Dec", current_day, YEAR_IN_FOLDER_NAME and "with year in folder name" or "")

  if len(sys.argv) > 1:
    for i in range(1, len(sys.argv)):
      arg = sys.argv[i]
      if arg != None and arg.isdigit():
        if len(arg) == 4:
          current_year = int(arg)
          YEAR_IN_FOLDER_NAME = True
        elif 1 <= len(arg) <= 2:
          current_day = int(arg)
        else:
          print("Error: Invalid argument")
          sys.exit(1)

  # Read session.txt file and put it in the environnement variable AOC_SESSION


  download_input_txt_file(current_day, current_year, YEAR_IN_FOLDER_NAME)