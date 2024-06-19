#!/usr/bin/env python3
# coding: utf-8
import rospkg

"""
  - {user     : ""}
  - {assistant: ""}
"""

def read_file_and_flatten_text(file_path):
    with open(file_path, 'r') as file:
        lines = file.read()  # ファイルの内容をリストとして読み込む
        # print(lines)
        # flattened_text = ''
        # for line in lines:
            # lines = lines.replace('\n', '\\n')
        lines = lines.replace('\\n===\\n', '}\n  - {user     : "')
        lines = lines.replace('\\n---\\n', '"}\n  - {assistant: "')
        lines = lines.replace('END', 'END"')
            # flattened_text += line
        return lines[2:]

file_path = "/home/sobits/catkin_ws/src/ollama_python/tuning_text/gpsr50th_turning.txt"
flattened_text = read_file_and_flatten_text(file_path) + "}"
# print(flattened_text)
file = open("/home/sobits/catkin_ws/src/ollama_python/tuning_text/gpsr50th_turning_.txt", 'w')
lines = file.write(flattened_text)