def calculateGPA(pair):
    """
    从传入pair列表[score,weight]来计算GPA
    :param pair: 以[score,weight]格式传入的列表
    :return: 最终GPA
    """
    total = 0
    scores = 0
    for i in range(len(pair)):
        total += float(pair[i][1])
        scores += float(pair[i][0]) * float(pair[i][1])
    final = scores / total
    return (final - 50) / 10
