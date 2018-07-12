import re
from sys import argv, exit

def parseFile(fileName):
    with open(fileName) as file:
        data = file.read()
        pattern = r'(\d+)\s*\n\s*(\d+):(\d+):(\d+),(\d+)\s+-->\s+(\d+):(\d+):(\d+),(\d+)\s*\n\s*((.+\n)+)'
        return re.findall(pattern, data)


def editRecords(offset, records):
    result = []
    for record in records:
        record = list(record)

        record[4] = int(record[4]) + offset*1000
        record[3] = int(record[3]) + (record[4] // 1000)
        record[2] = int(record[2]) + (record[3] // 60)
        record[1] = int(record[1]) + (record[2] // 60)

        record[8] = int(record[8]) + offset * 1000
        record[7] = int(record[7]) + (record[8] // 1000)
        record[6] = int(record[6]) + (record[7] // 60)
        record[5] = int(record[5]) + (record[6] // 60)

        for i in range(1, 9):
            if record[i] < 0:
                print("Offset is too negative")
                exit(0)

        for i in range(1, 4):
            record[i] %= 60
            record[i+4] %= 60
        record[4] %= 1000
        record[8] %= 1000

        for i in range(1, 9):
            record[i] = int(record[i])

        result.append(record)
    return result


def saveResult(fileName, result):
    with open(fileName, "w") as file:
        for record in result:
            file.write(record[0] + "\n" +
                       str(record[1]).zfill(2) + ":" +
                       str(record[2]).zfill(2) + ":" +
                       str(record[3]).zfill(2) + "," +
                       str(record[4]).zfill(3) +
                       " --> " +
                       str(record[5]).zfill(2) + ":" +
                       str(record[6]).zfill(2) + ":" +
                       str(record[7]).zfill(2) + "," +
                       str(record[8]).zfill(3) + "\n")
            for line in record[9:-1]:
                file.write(line)
            file.write("\n")


if __name__ == "__main__":
    if len(argv) != 3 and len(argv) != 4:
        print("Wrong number of arguments")
        exit(0)
    try:
        num = float(argv[2])
    except ValueError:
        print("Offset must be a number")
        exit(0)
    if len(argv) == 4:
        saveResult(argv[3], editRecords(num, parseFile(argv[1])))
    else:
        saveResult(argv[1], editRecords(num, parseFile(argv[1])))
