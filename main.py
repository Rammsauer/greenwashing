import time
from os import system

input_string = []
output_string = []
readme_string = ""

Github_Username = ""
Github_Token = ""

def write_nextline():
    with open('inputFile') as f:
        input_string = f.readlines()
    with open('outputFile') as f:
        output_string = f.readlines()

    file = open('outputFile', 'a')
    readme = open('README.md', 'w')

    file.write(f'{input_string[len(output_string)]}')
    file.close()

    with open('outputFile') as f:
        readme_string = f.read().rstrip()
    readme.write('<pre>\n' + readme_string + '\n</pre>')
    readme.close()

    create_commit()


def git_login():
    system(
        f"git remote set-url origin https://{Github_Username}:{Github_Token}@github.com/{Github_Username}/greenwashing.git")


def create_commit():
    system("git fetch")
    system("git add README.md")
    system("git add outputFile")
    system(f"git commit -m \"Quasimoto - Greenery\"")
    system("git push")


while True:
    git_login()
    write_nextline()
    time.sleep(3600 * 3)
