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
        self.surface = ""
        self.pos = ""
        self.base = ""
        self.pos1 = ""

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
                tree = parser.parse(i)
                print(tree)
                ofp.write(tree.toString(CaboCha.CABOCHA_FORMAT_LATTICE))



class Chunk():
    """
    40
    に加えて，文節を表すクラスChunkを実装せよ．このクラスは形態素（Morphオブジェクト）のリスト（morphs），
    係り先文節インデックス番号（dst），係り元文節インデックス番号のリスト（srcs）をメンバ変数に持つこととする．
    さらに，入力テキストのCaboChaの解析結果を読み込み，１文をChunkオブジェクトのリストとして表現し，8
    文目の文節の文字列と係り先を表示せよ．第5章の残りの問題では，ここで作ったプログラムを活用せよ．
    """
    morphs = []
    dst = 0
    srcs = []

    def __init__(self):
        self.morphs = []
        self.dst = 0
        self.srcs = []

from collections import defaultdict

def problem_41(printout=False):
    sentences = []

    with open("neko.cabocha") as fp:
        chunk = Chunk()
        chunks = []
        for s in fp:
            # print("原文：", s)
            if s[0] == '*':
                if len(chunk.morphs) > 0:
                    chunks.append(chunk)
                chunk = Chunk()

                firstline = s.split(' ')
                chunk.dst = int(firstline[2].strip('D'))
                # 係り受けIDはリストのindexに相当

            elif s.find('EOS') >= 0:
                    for i, c in enumerate(chunks):
                        if c.dst != -1:
                            chunks[c.dst-1].srcs.append(i)
                    if len(chunk.morphs)>0:
                        chunks.append(chunk) # sentencesにchunkのリストをappendする前に現在のchunkも追加しておく
                    chunk = Chunk()
                    sentences.append(chunks)
                    chunks = []

            else:
                # 形態素の行
                morph = Morph()
                dummy = s.split('\t')
                elements = dummy[1].split(',')
                morph.surface = dummy[0]
                morph.pos1 = elements[1]
                morph.base = elements[5]
                morph.pos = elements[0]
                chunk.morphs.append(morph)

        if printout:
            for i, chunk in enumerate(sentences[7]):
                print("{0}:{1}".format(i, chunk.dst))

                for morph in chunk.morphs:
                   print("MORPH : {0}".format(morph.surface))

            for i, chunk in enumerate(sentences[8]):
                print("{0}:{1}".format(i, chunk.dst))

                for morph in chunk.morphs:
                   print("MORPH : {0}".format(morph.surface))

    return sentences

def generate_tab_sequence(chunks, chunk):
    lst = []
    for src in chunk.srcs:
        lst.append(''.join([ x.surface for x in chunks[src].morphs
                             if x.pos != "記号" ]))

    return '\t'.join(lst)




def problem_42():
    """
    42. 係り元と係り先の文節の表示
    係り元の文節と係り先の文節のテキストをタブ区切り形式ですべて抽出せよ．
    ただし，句読点などの記号は出力しないようにせよ．
    :return:
    """
    sentences = problem_41()
    print(len(sentences))
    for sentence in sentences:
        for chunk in sentence:
            s = ''
            if chunk.src != -1:
                print("かかり先：{0}, かかり元:  {1}".format(chunk.dst, generate_tab_sequence(sentence, chunk)))

def problem_43():
    """
    名詞を含む文節が，動詞を含む文節に係るとき，これらをタブ区切り形式で抽出せよ．
    ただし，句読点などの記号は出力しないようにせよ．
    :return:
    """

    sentences = problem_41()

    for sentence in sentences:
        for chunk in sentence:
            for morph in chunk.morphs:
                if morph.pos == '名詞':
                    # かかり先に動詞が含まれるかを調べる
                    if chunk.dst != -1:
                        for i in sentence[chunk.dst].morphs:
                            if i.pos == '動詞':
                                print(generate_tab_sequence(sentence, chunk))
                                break


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

    with open("neko.cabocha") as fp:

        for s in fp:
            sentence = ""
            parsed = mcb.parse(s)
            Morphs = []
            s = s.replace('\n', '')
            if len(parsed) > 0:
                p = parsed.split('\n')

                for m in p:
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

                sentences.append((s, Morphs))
    """
    for s in sentences:
       print("結果 : {0}".format(s[0]))
       for mrp in s[1]:
           print("{0}".format(mrp.surface))
    """
    with open(CABOCHA_FILE) as fp:
        for i in fp:
            print(i)


if __name__ == '__main__':
    problem_43()