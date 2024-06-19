# coding: utf-8
import os


def flatten_text(lines):
    flattened_text = ''
    for line in lines:
        line = line.replace('\n', '\\n')  # 改行を"\n"に置換
        line = line.replace('\t', '\\t')  # 改行を"\n"に置換
        flattened_text += line
    return flattened_text


def read_file_and_fix_text(file_path):
    with open(file_path, 'r') as file:
        lines = file.read()  # ファイルの内容をリストとして読み込む
        lines = lines.replace('次の指示文をタスク分岐してください。\n指示文「', 'input text : ')
        lines = lines.replace('」', '')
        lines = lines.split("---")[:-1]
        lines = ('---'.join(lines))
        lines = lines.split("\n")[:-1]
        lines = ('\n'.join(lines))
        return lines


def main():
    dir_path = "/home/sobits/catkin_ws/src/ollama_python/tuning_text"
    files = os.listdir(dir_path)

    text_list = ""

    for file in files:
        if (".txt" in file):
            text_list += "\n===\n" + read_file_and_fix_text(dir_path + "/" + file)
    # text_list = text_list.split("\n===\n")[:-1]
    # text_list = ('\n===\n'.join(text_list))
    # print(text_list)
    text_list = flatten_text(text_list)
    file = open("/home/sobits/catkin_ws/src/ollama_python/tuning_text/gpsr50th_turning.txt", 'w')
    lines = file.write(text_list)


if __name__ == "__main__": 
    main()
