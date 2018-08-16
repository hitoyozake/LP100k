# -* encoding: utf-8 *-
import CaboCha
import MeCab
"""
第5章: 係り受け解析
夏目漱石の小説『吾輩は猫である』の文章（neko.txt）をCaboChaを使って係り受け解析し，
その結果をneko.txt.cabochaというファイルに保存せよ．
このファイルを用いて，以下の問に対応するプログラムを実装せよ．
"""
CABOCHA_FILE = "neko.cabocha"

class Morph():
    surface = "" # 表層形
    pos = "" # 品詞
    base = "" # 基本形
    pos1 = "" # 品詞細分形1

    def __init__(self):
        """
        """





def get_kakariuke():
    """

    :return:
    """
    import sys, os


    if not os.path.exists(CABOCHA_FILE):
        strs = []
        with open("./neko.txt") as fp:
            strs = fp.readlines()

        parser = CaboCha.Parser("-d /usr/local/lib/mecab/dic/mecab-ipadic-neologd")

        with open(CABOCHA_FILE, "w") as ofp:
            for i in strs:
                r = parser.parseToString(i)
                print(r)
                ofp.write(r)


def problem_40():
    """
    40. 係り受け解析結果の読み込み（形態素）
    形態素を表すクラスMorphを実装せよ．このクラスは表層形（surface），基本形（base），
    品詞（pos），品詞細分類1（pos1）をメンバ変数に持つこととする．
    さらに，CaboChaの解析結果（neko.txt.cabocha）を読み込み，
    各文をMorphオブジェクトのリストとして表現し，3文目の形態素列を表示せよ．
    :return:
    """

    # 形態素解析を行う
    mcb = MeCab.Tagger("-d /usr/local/lib/mecab/dic/mecab-ipadic-neologd")
    sentences = []

    with open("neko.txt") as fp:
        MorphList = []
        for s in fp:
            parsed = mcb.parse(s)
            Morphs = []

            for m in parsed:
                if m != 'EOS' and m != '':
                    y = m.split('\t')
                    molphens = y[1].split(',')
                    # print("{0}:{1}".format(y[0], molphens))
                    mlp = Morph()
                    mlp.surface = y[0]
                    mlp.pos1 = molphens[1]
                    mlp.base = molphens[5]
                    mlp.pos = molphens[0]

                    Morphs.append(mlp)
                MophList.append(Morphs)

        """
            
        """


    with open(CABOCHA_FILE) as fp:
        for i in fp:
            print(i)


if __name__ == '__main__':
    get_kakariuke()