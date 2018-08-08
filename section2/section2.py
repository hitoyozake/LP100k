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


if __name__ == "__main__":
    print("section2")
    problem_11()