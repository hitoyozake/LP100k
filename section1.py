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

def problem_04():
    """
    04. 元素記号
"Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."という文を単語に分解し，1, 5, 6, 7, 8, 9, 15, 16, 19番目の単語は先頭の1文字，それ以外の単語は先頭に2文字を取り出し，取り出した文字列から単語の位置（先頭から何番目の単語か）への連想配列（辞書型もしくはマップ型）を作成せよ．
    :return:
    """

    s = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."

    mono = [1, 5, 6, 7, 8, 9, 15, 16, 19]

    s = s.replace(',', '').replace(',', '')

    dic = {}

    for index, word in enumerate(s.split(' ')):
        print("{0} : {1}".format(index, word))
        if index+1 in mono:
            dic[word[0]] = word
        else:
            dic[word[0:2]] = word

    print("Dictionary: {0}".format(dic))

    return dic


def get_n_gram(s, n):
    """
    n-gramを作成する
    :param s: input string or iterative object
    :param n: n
    :return: n-gram list[str]
    """
    out = []
    for i in range(0, len(s)-n+1):
        out.append(s[i:i+n])
    return out

def problem_05():
    """
    与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．この関数を用い，"I am an NLPer"という文から単語bi-gram，文字bi-gramを得よ．
    :return:
    """
    s = "I am an NLPer"
    char_out = get_n_gram(s, 2)
    print(char_out)

    word_out = get_n_gram(s.split(' '), 2)

    print(word_out)

def problem_06():
    """
    06. 集合
"paraparaparadise"と"paragraph"に含まれる文字bi-gramの集合を，それぞれ, XとYとして求め，XとYの和集合，積集合，差集合を求めよ．さらに，'se'というbi-gramがXおよびYに含まれるかどうかを調べよ．
    :return:
    """
    s1, s2 = "paraparaparadise", "paragraph"

    s1 = get_n_gram(s1, 2)
    s2 = get_n_gram(s2, 2)

    s1 = set(s1)
    s2 = set(s2)

    wa_set = s1 | s2
    seki_set = s1 & s2

    print(wa_set)
    print(seki_set)

    # 差集合
    diff1, diff2 = s1-s2, s2-s1

    print(diff1!=diff2) # true
    print(diff1)
    print(diff2)

    if 'se' in s1:
        print('se in s1')
    if 'se' in s2:
        print('se in s2')

def problem_07(x, y, z):
    """
    07. テンプレートによる文生成
引数x, y, zを受け取り「x時のyはz」という文字列を返す関数を実装せよ．さらに，x=12, y="気温", z=22.4として，実行結果を確認せよ．


    :return:
    """

    out =  "{0}時の{1}は{2}".format(x, y, z)

    print(out)

    return out

def problem_08(s):
    """
    08. 暗号文
与えられた文字列の各文字を，以下の仕様で変換する関数cipherを実装せよ．

英小文字ならば(219 - 文字コード)の文字に置換
その他の文字はそのまま出力
この関数を用い，英語のメッセージを暗号化・復号化せよ．
    :param s:
    :return:
    """
    out = ""
    for c in s:
        if c.islower():
            out += chr(219 - ord(c))
        else:
            out += c

    print(out)

    return out

def problem_09(s):

    """
    09. Typoglycemia
スペースで区切られた単語列に対して，各単語の先頭と末尾の文字は残し，それ以外の文字の順序をランダムに並び替えるプログラムを作成せよ．ただし，長さが４以下の単語は並び替えないこととする．適当な英語の文（例えば"I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."）を与え，その実行結果を確認せよ．
    :param s:
    :return:
    """

    splited = s.split(' ')
    med = splited[1:-1]
    import random
    random.shuffle(med)
    out = splited[0] + " " + " ".join(med) + " " + splited[-1]

    print(med)

    print(out)

    return out

if __name__ == '__main__':
    problem_09("I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind .")
