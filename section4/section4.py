# -* encoding:utf-8 *-
import MeCab

"""
第4章: 形態素解析
夏目漱石の小説『吾輩は猫である』の文章（neko.txt）をMeCabを使って形態素解析し，
その結果をneko.txt.mecabというファイルに保存せよ．このファイルを用いて，
以下の問に対応するプログラムを実装せよ．

"""

def load_neco():
    with open('neko.txt') as fp:
        strs = []
        for s in fp:
            s = s.replace('\n', '')
            # print(s)
            strs.append(s)
        return strs


def converter(word):
    m = MeCab.Tagger("-d /usr/local/lib/mecab/dic/mecab-ipadic-neologd")

    return m.parse(word).split('\t')[1].split(',')[6]

def problem_30():
    """
    形態素解析結果（neko.txt.mecab）を読み込むプログラムを実装せよ．
    ただし，各形態素は表層形（surface），基本形（base），品詞（pos），
    品詞細分類1（pos1）をキーとするマッピング型に格納し，1文を形態素（マッピング型）のリストとして表現せよ．
    第4章の残りの問題では，ここで作ったプログラムを活用せよ．
    :return:
    """
    m = MeCab.Tagger("-d /usr/local/lib/mecab/dic/mecab-ipadic-neologd")

    lines = load_neco()

    output = []

    for l in lines:
        parsed = m.parse(l).split('\n')

        for x in parsed:
            if x != 'EOS' and x != '':
                dictionary = {}

                y = x.split('\t')
                molphens = y[1].split(',')
                # print("{0}:{1}".format(y[0], molphens))
                dictionary['surface'] = y[0]
                dictionary['pos1'] = molphens[1]
                dictionary['base'] = molphens[5]
                dictionary['pos'] = molphens[0]
                # print(dictionary)
                output.append(dictionary)

    return output

def problem_31():
    """
    31. 動詞
動詞の表層形をすべて抽出せよ．
    :return:
    """
    x = problem_30()

    for i in x:
        if i['pos'] == '動詞':
            print(i['surface'])

def problem_32():
    """
    32. 動詞の原形
動詞の原形をすべて抽出せよ．
    :return:
    """
    x = problem_30()

    for i in range(len(x)-1):
        if x[i]['pos'] == '動詞':
            print("表層形 : {0}, 原形 : {1}".format(x[i]['surface'], converter(x[i]['surface']+x[i+1]['surface'])))


def problem_33():
    """
    33. サ変名詞
    サ変接続の名詞をすべて抽出せよ．
    :return:
    """

    x = problem_30()

    m = MeCab.Tagger("-d /usr/local/lib/mecab/dic/mecab-ipadic-neologd")


    for i in x:
        if i['pos'] == '名詞':
            if m.parse(i['surface']).split('\t')[1].split(',')[1] == 'サ変接続':
                print(i['surface'])


def problem_34():
    """
    34. 「AのB」
    2つの名詞が「の」で連結されている名詞句を抽出せよ．
    :return:
    """

    x = problem_30()

    for i in range(2, len(x) - 2):
        if x[i-2]['pos'] == '名詞' and x[i-1]['surface'] == 'の' and x[i]['pos'] == '名詞':
            print("{0}{1}{2}".format(x[i-2]['surface'], x[i-1]['surface'], x[i]['surface']))



def problem_35():
    """
    35. 名詞の連接
名詞の連接（連続して出現する名詞）を最長一致で抽出せよ
    :return: 
    """
    x = problem_30()

    for index in range(len(x)):
        if x[index]['pos'] == '名詞':
            count = 1
            for i2 in range(min(len(x), index+1), len(x)):
                if x[index]['surface'] == x[i2]['surface']:
                    count += 1
                else:
                    break
            if count >= 2:
                print("{1} count:{0}".format(count, x[index]['surface']))


def problem_36():
    """
    36. 単語の出現頻度
文章中に出現する単語とその出現頻度を求め，出現頻度の高い順に並べよ．
    :return:
    """
    x = problem_30()

    dictionary = {}

    from collections import defaultdict
    # dictionary = defaultdict(int)
    dictionary = defaultdict(lambda : 0)

    for i in x:
        """
        if i['surface'] not in dictionary:
            dictionary[i['surface']] = 0
        dictionary[i['surface']] += 1
        """
        dictionary[i['surface']] += 1

    print(dictionary)





if __name__ == '__main__':
    problem_36()

