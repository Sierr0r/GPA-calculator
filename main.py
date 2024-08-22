import GPAcalculator
import csvreader


def main():
    address = input(
        "输入要计算的csv文件路径(默认为同目录下1.csv)\n"
    )
    if address == '':
        address = '1.csv'
    GPA = GPAcalculator.calculateGPA(csvreader.csvreader(address))
    print('{0:.2f}'.format(GPA))


if __name__ == "__main__":
    main()
