# -* encoding: utf-8 *-
import CaboCha
"""
第5章: 係り受け解析
夏目漱石の小説『吾輩は猫である』の文章（neko.txt）をCaboChaを使って係り受け解析し，
その結果をneko.txt.cabochaというファイルに保存せよ．
このファイルを用いて，以下の問に対応するプログラムを実装せよ．
"""

def get_kakariuke():
    """

    :return:
    """
    import sys, os

    CABOCHA_FILE = "neko.cabocha"

    if not os.path.exists(CABOCHA_FILE):
        r = ""
        with open("./neko.txt") as fp:
            strs = fp.readlines()

            parser = CaboCha.Parser("-d /usr/local/lib/mecab/dic/mecab-ipadic-neologd")

            for i in strs:
                r = parser.parseToString(i)
                print(r)



if __name__ == '__main__':
    get_kakariuke()