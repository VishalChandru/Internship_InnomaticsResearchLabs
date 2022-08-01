if __name__ == '__main__':
    records = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name,score])
    scores = set()
    for i in range(len(records)):
        scores.add(records[i][1])
    scores = list(sorted(scores))
    stu = []
    for j in range(len(records)):
        if records[j][1] == scores[1]:
            stu.append(records[j][0])
    stu = sorted(stu)
    for k in range(len(stu)):
        print(stu[k])