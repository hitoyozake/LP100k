# -* encoding: utf-8 *-

INPUT = "hightemp.txt"


def problem_10():
    """
    10. 行数のカウント
行数をカウントせよ．確認にはwcコマンドを用いよ．
    :return:
    """
    count = 0

    with open(INPUT) as fp:
        while(fp.readline()):
            count += 1

    print(count)

    return count

def problem_11():
    """

    :return:
    """
    with open(INPUT) as fp:

        strs = fp.readlines()
        out = []
        for i in strs:
            out.append(i.replace('\t', ' '))

        out = '\n'.join(out)

        print(out)

        return out


    out = input.replace("\t", " ")
    print(out)

    return out

def problem_12():
    with open(INPUT) as fp:
        strs = fp.readlines()

        col1 = []
        col2 = []
        for s in strs:
            c1, c2 = s.split("\t")[0:2]
            col1.append(c1)
            col2.append(c2)

    with open("col1.txt", "w") as fp:
        fp.write("\n".join(col1))
    with open("col2.txt", "w") as fp:
        fp.write("\n".join(col2))

def problem_13():
    c1, c2 = [], []
    with open("col1.txt") as fp:
        c1 = fp.readlines()
    with open("col2.txt") as fp:
        c2 = fp.readlines()

    out = []

    for x, y in zip(c1, c2):
        out.append(x.replace('\n', '') +"\t"+y.replace('\n', ''))

    out = "\n".join(out)

    print(out)

    return out

def problem_14(n):
    """
    14. 先頭からN行を出力
自然数Nをコマンドライン引数などの手段で受け取り，入力のうち先頭のN行だけを表示せよ．確認にはheadコマンドを用いよ．
    :param n:
    :return:

    """
    with open(INPUT) as fp:
        for i in range(n):
            line = fp.readline()
            line = line.replace('\n', '')
            line = line.replace('\r', '')
            print(line)
            if line is None:
                break

def problem_15(n):
    """
    15. 末尾のN行を出力
自然数Nをコマンドライン引数などの手段で受け取り，入力のうち末尾のN行だけを表示せよ．確認にはtailコマンドを用いよ．
    :param n:
    :return:
    """
    with open(INPUT) as fp:
        strs = []

        for line in fp:
            strs.append(line)

        for i in strs[-n::1]:
            line = i
            line = line.replace('\n', '')
            line = line.replace('\r', '')
            print(line)
            if line is None:
                break

def problem_16(n):
    """
    16. ファイルをN分割する
自然数Nをコマンドライン引数などの手段で受け取り，入力のファイルを行単位でN分割せよ．同様の処理をsplitコマンドで実現せよ．


    :param n:
    :return:
    """
    with open(INPUT) as fp:
        strs = []

        for line in fp:
            strs.append(line)

        l = len(strs)

        for i in range(n-1):
            with open("{0}.txt".format(i), "w") as ofp:
                for j in range(int(l/n)):
                    index=j + i*l
                    ofp.write(strs[j + int(i*l/n)])

        with open("{0}.txt".format(n-1), "w") as ofp:
            for i in range(int((n-1)*l/n), len(strs)):
                ofp.write(strs[i])


def problem_17():
    col1 = set()
    with open(INPUT) as fp:
        for i in fp:
            col1.add(i.split('\t')[0])

    for i in col1:
        print(i)

def problem_18():
    strs = []
    with open(INPUT) as fp:
        strs = [i.split('\t') for i in fp]

    strs.sort(key=lambda x:x[2])

    print(strs)


if __name__ == "__main__":
    print("section2")
    problem_18()