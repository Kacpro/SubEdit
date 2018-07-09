import re


def parseFile(fileName):
    with open(fileName) as file:
        data = file.read()
        pattern = r'(?P<num>\d+)\s*\n\s*(?P<hourStart>\d+):(?P<minStart>\d+):(?P<secStart>\d+),(?P<msecStart>\d+)\s+-->\s+(?P<hourEnd>\d+):(?P<minEnd>\d+):(?P<secEnd>\d+),(?P<msecEnd>\d+)\s*\n\s*(?P<text>(.+\n)+)'
        for record in re.finditer(pattern, data):
            print(record)





if __name__ == "__main__":
    print("Work in progress")
