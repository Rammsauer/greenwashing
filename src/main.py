import datetime
import time
from os import system

import schedule
import Constants as c

input_string = []
output_string = []
readme_string = ""


def main():
    while True:
        schedule.run_pending()
        time.sleep(1)


def build_commit_time_list():
    for hour in range(11):
        c.commit_time_list.append(datetime.time(hour=2 * hour, minute=0, second=0))


def schedule_job():
    for time in c.commit_time_list:
        schedule.every().day.at(str(time)).do(write_nextline)


def write_nextline():
    with open('inputFile') as f:
        input_string = f.readlines()
    with open('outputFile') as f:
        output_string = f.readlines()

    file = open('outputFile', 'a')
    readme = open('../README.md', 'w')

    file.write(f'{input_string[len(output_string)]}')
    file.close()

    with open('outputFile') as f:
        readme_string = f.read().rstrip()
    readme.write('<pre>\n' + readme_string + '\n</pre>')
    readme.close()

    create_commit()


def git_login():
    system(f"git remote set-url origin https://{c.Github_Username}:{c.Github_Token}@github.com/{c.Github_Username}/greenwashing.git")


def create_commit():
    system("git add README.md")
    system("git add outputFile")
    system(f"git commit -m \"Quasimoto - Greenery\"")
    system("git push")


git_login()
build_commit_time_list()
schedule_job()
main()