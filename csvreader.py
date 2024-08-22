def csvreader(address='1.csv'):
    """
    用于从csv中读取分数与权重
    :param address: csv文件地址（默认同目录下1.csv）
    :return: 返回嵌套列表，内层列表为[score,weight]形式
    """
    f = open(address, 'r', encoding='utf-8')
    list1 = []
    for line in f:
        line1 = line.strip()
        pair = line1.split(',')
        list1.append(pair)
    return list1


if __name__ == '__main__':
    print(csvreader())
