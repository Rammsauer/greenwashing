import time

inputString = ""
readmeString = ""
outputString = ""


def main():
    while True:
        writeNextLine()
        time.sleep(5)


def writeNextLine():
    with open('inputFile') as f:
        inputString = f.readlines()
    with open('outputFile') as f:
        outputString = f.readlines()

    print(f'{outputString}')

    file = open('outputFile', 'a')
    readme = open('README.md', 'w')

    file.write(f'{inputString[len(outputString)]}')

    with open('outputFile') as f:
        readmeString = f.read().rstrip()
    readme.write('<pre>\n' + readmeString + '\n</pre>')


main()
