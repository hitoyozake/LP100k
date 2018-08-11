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
        return fp.readlines()

def problem_30():
    """
    形態素解析結果（neko.txt.mecab）を読み込むプログラムを実装せよ．
    ただし，各形態素は表層形（surface），基本形（base），品詞（pos），
    品詞細分類1（pos1）をキーとするマッピング型に格納し，1文を形態素（マッピング型）のリストとして表現せよ．
    第4章の残りの問題では，ここで作ったプログラムを活用せよ．
    :return:
    """
    m = MeCab.Tagger("-Ochasen -d /usr/local/lib/mecab/dic/mecab-ipadic-neologd")

    lines = load_neco()

    for s in lines:
        print(m.parse(s))

def problem_31():
    """

    :return:
    """


if __name__ == '__main__':
    problem_30()

