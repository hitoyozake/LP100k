# -* encoding:utf-8 *-
# 正規表現
import json
import re

def load_json():
    data = None
    with open("jawiki-country.json", encoding='utf-8') as fp:
        data = []
        for i in fp:
            data.append(json.loads(i))

    return data

def extract_about_UK(ls):
    d = []

    for i in ls:
        if 'イギリス' in i['text'] or 'イギリス' in i['title']:
            d.append(i)

    return d


def problem_20():
    """
    20. JSONデータの読み込み
    Wikipedia記事のJSONファイルを読み込み，「イギリス」に関する記事本文を表示せよ．問題21-29では，ここで抽出した記事本文に対して実行せよ．
    :return:
    """
    d = load_json()

    d = extract_about_UK(d)

    for i in d:
        print(i)

def problem_21():
    """
    21. カテゴリ名を含む行を抽出
    記事中でカテゴリ名を宣言している行を抽出せよ．
    :return:
    """
    d = load_json()

    d = extract_about_UK(d)

    for i in d:
        print("******************")
        x = i['text'].split('\n')
        for j in x:
            if 'Category' in j:
                print(j)
        print("******************")

def problem_22():
    """
    22. カテゴリ名の抽出
    記事のカテゴリ名を（行単位ではなく名前で）抽出せよ．
    :return:
    """
    d = extract_about_UK(load_json())

    for i in d:
        x = i['text'].split('\n')
        for j in x:
            if re.match('.+\[Category:.+', j):
                print(j)

if __name__ == '__main__':
    problem_22()