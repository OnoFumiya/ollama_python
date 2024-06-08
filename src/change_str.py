#!/usr/bin/env python3
# coding: utf-8
import rospkg

def read_file_and_flatten_text(file_path):
    with open(file_path, 'r') as file:
        lines = file.read()  # ファイルの内容をリストとして読み込む
        print(lines)
        flattened_text = ''
        for line in lines:
            line = line.replace('\n', '\\n')  # 改行を"\n"に置換
            line = line.replace('\t', '\\t')  # 改行を"\n"に置換
            flattened_text += line
            # flattened_text += line.strip()  # 行末の改行を削除して、1行の文字列に追加
        return flattened_text

file_path = 'text.txt'
flattened_text = read_file_and_flatten_text(file_path)
print(flattened_text)
file = open("temp.txt", 'w')
lines = file.write(flattened_text)
