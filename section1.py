# -* encoding: utf-8 *-

def problem_00():
    s = "stressed"
    reversed = ""
    for i in s[::-1]:
        reversed += i

    print("input:{0}, output: {1}".format(s, reversed))

    return reversed

def problem_01():
    """
    01. 「パタトクカシーー」
    「パタトクカシーー」という文字列の1,3,5,7文字目を取り出して連結した文字列を得よ．
    :return: ans
    """
    s = "パタトクカシーー"
    out = s[::2]

    print("input:{0}, output: {1}".format(s, out))

    return out

def problem_02():
    """
    02. 「パトカー」＋「タクシー」＝「パタトクカシーー」
「パトカー」＋「タクシー」の文字を先頭から交互に連結して文字列「パタトクカシーー」を得よ．
    :return:
    """
    s1, s2 = "パトカー", "タクシー"
    out = ""
    for i in range(len(s1)):
        out += s1[i] + s2[i]

    print("input:{0}, output: {1}".format(s1+s2, out))

    return out

def problem_03():
    """
    03. 円周率
"Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."という文を単語に分解し，各単語の（アルファベットの）文字数を先頭から出現順に並べたリストを作成せよ．
    :return:out
    """
    s = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."

    # 文字列の洗浄
    s = s.replace('.', '').replace(',', '')

    out = []
    # 単語ごとに分解
    out = [len(word) for word in s.split(' ')]

    for i, j in zip(s.split(' '), out):
        print("{0} : {1}".format(i, j))

    return out





if __name__ == '__main__':
    problem_03()