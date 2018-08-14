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
    parser = CaboCha.Parser("-d /usr/local/lib/mecab/dic/mecab-ipadic-neologd")

    r = parser.parseToString("吾輩は猫である．名前はまだない．今日は大きいおにぎりを食べた．")

    print(r)


if __name__ == '__main__':
    get_kakariuke()