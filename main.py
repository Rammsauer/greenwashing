import datetime
import time
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
    for hour in range(10):
        c.commit_time_list.append(datetime.time(hour=14, minute=45, second=hour*5))


def schedule_job():
    for time in c.commit_time_list:
        schedule.every().day.at(str(time)).do(write_nextline)


def write_nextline():
    with open('inputFile') as f:
        input_string = f.readlines()
    with open('outputFile') as f:
        output_string = f.readlines()

    print(f'{output_string}')

    file = open('outputFile', 'a')
    readme = open('README.md', 'w')

    file.write(f'{input_string[len(output_string)]}')

    with open('outputFile') as f:
        readme_string = f.read().rstrip()
    readme.write('<pre>\n' + readme_string + '\n</pre>')


build_commit_time_list()
schedule_job()
main()
