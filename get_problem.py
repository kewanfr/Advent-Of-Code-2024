# Simple script to download problem from Advent of Code
# Don't forget to put your session token in session.txt
# You can find it in your browser cookies
# This script will create a folder for each day, and put the input file in it

# You can also call it with arguments to specify the date, for example:
# python get_problem.py 2023 1
# will download the problem for the 1st December 2023

# Credits:
# António Ramadas (https://github.com/antonio-ramadas) for https://github.com/antonio-ramadas/aoc-to-markdown
# Kyle Farnung (https://github.com/kfarnung) for https://github.com/kfarnung/aoc-to-markdown
# Kéwan (https://github.com/kewanfr) for this script
# I used parts of their codes to make this script, so thanks to them !


import os, sys
from datetime import datetime

import requests
from bs4 import BeautifulSoup
from get_input_file import download_input_txt_file


YEAR_IN_FOLDER_NAME = False
# If True, the folder will be named for ex "2020 Dec" instead of "Dec"

DOWNLOAD_INPUT_FILE = True
# If True, the input file will be downloaded in the folder

current_year = datetime.now().year
# Change this if you want to download input files from another year

current_day = datetime.now().day

if len(sys.argv) > 1:
  for i in range(1, len(sys.argv)):
    arg = sys.argv[i]
    if arg == "-p":
      DOWNLOAD_INPUT_FILE = False
    if arg != None and arg.isdigit():
      if len(arg) == 4:
        current_year = int(arg)
        YEAR_IN_FOLDER_NAME = True
      elif 1 <= len(arg) <= 2:
        current_day = int(arg)
      else:
        print("Error: Invalid argument")
        sys.exit(1)

print(
  "Downloading problem file for",
  current_year,
  "Dec",
  current_day,
  YEAR_IN_FOLDER_NAME and "with year in folder name" or "",
)


def get_html(year, day):
  url = f"https://adventofcode.com/{year}/day/{day}"
  response = requests.get(url, cookies={"session": os.getenv("AOC_SESSION")})

  if response.status_code != 200:
    raise ValueError(
      f"Querying the url {url} resulted in status code {response.status_code} with the following "
      f"text: {response.text}"
    )

  return response.text


# Simplification of https://github.com/dlon/html2markdown/blob/master/html2markdown.py
def html_tags_to_markdown(tag, is_first_article):
  children = tag.find_all(recursive=False)

  if tag.name != "code":
    for child in children:
      html_tags_to_markdown(child, is_first_article)

  if tag.name == "h2":
    style = "#" if is_first_article else "##"
    tag.insert_before(f"{style} ")
    tag.insert_after("\n\n")
    tag.unwrap()
  elif tag.name == "p":
    tag.insert_after("\n")
    tag.unwrap()
  elif tag.name == "em":
    style = "**" if tag.has_attr("class") and tag["class"] == "star" else "**"
    tag.insert_before(style)
    tag.insert_after(style)
    tag.unwrap()
  elif tag.name == "a":
    tag.insert_before("[")
    href = tag["href"]
    if href.startswith("/"):
      href = f"https://adventofcode.com{href}"
    tag.insert_after(f"]({href})")
    tag.unwrap()
  elif tag.name == "span":
    tag.insert_before("*")
    tag.insert_after("*")
    tag.unwrap()
  elif tag.name == "ul":
    tag.unwrap()
  elif tag.name == "li":
    tag.insert_before(" - ")
    tag.insert_after("\n")
    tag.unwrap()
  elif tag.name == "code":
    if "\n" in tag.text:
      tag.insert_before("```\n")
      tag.insert_after("```")
    else:
      tag.insert_before("`")
      tag.insert_after("`")
    tag.unwrap()
  elif tag.name == "pre":
    tag.insert_before("")
    tag.insert_after("\n")
    tag.unwrap()
  elif tag.name == "article":
    pass
  else:
    raise ValueError(f"Missing condition for tag: {tag.name}")


def get_markdown(year, day):
  soup = BeautifulSoup(get_html(year, day), features="html.parser")

  articles = soup.body.main.findAll("article", recursive=False)
  content = ""

  for i, article in enumerate(articles):
    html_tags_to_markdown(article, i == 0)
    content += "".join([tag.string for tag in article.contents])

  content += f'\n[Original link](https://adventofcode.com/{year}/day/{day})'

  return content


file_dir = os.path.dirname(os.path.realpath(__file__))
if YEAR_IN_FOLDER_NAME:
  file_dir += str(current_year) + " "
file_dir = os.path.join(file_dir, "Dec " + str(current_day))

print(file_dir)
if not os.path.exists(file_dir):
  print(file_dir)
  os.makedirs(file_dir, exist_ok=False)

file_path = os.path.join(file_dir, "README.md")

markdown = get_markdown(current_year, current_day)


open(file_path, "w").write(markdown)

print("\nFichier du problème du jour récupéré avec succès !")

if DOWNLOAD_INPUT_FILE:
  download_input_txt_file(current_day, current_year, YEAR_IN_FOLDER_NAME)
