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
                dictionary['surface'] = molphens[6]
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


if __name__ == '__main__':
    problem_31()

