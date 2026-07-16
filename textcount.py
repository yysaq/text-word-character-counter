import re
import sys
def count_english_words(line: str) -> int:
    # 匹配所有连续英文字母作为一个单词，自动过滤标点、数字、空格
    words = re.findall(r'[a-zA-Z]+', line)
    return len(words)

def count_chinese_chars(line: str) -> int:
    # 匹配所有汉字，排除标点、数字、空格、英文、特殊符号
    chinese_chars = re.findall(r'[\u4e00-\u9fa5]', line)
    return len(chinese_chars)

def count_text(file_path: str):
    ch_total = 0
    en_total = 0
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            ch_total += count_chinese_chars(line)
            en_total += count_english_words(line)
    return ch_total, en_total

if __name__ == "__main__":
    
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
    else:
        file_path = input("请输入文本文件路径：").strip()

    try:
            result = count_text(file_path)
            print(f"中文字符数： {result[0]}")
            print(f"英文词数： {result[1]}")
    except FileNotFoundError:
            print(f"Error: File '{file_path}' not found.")
    except UnicodeDecodeError:
            print("Error: File encoding is not UTF-8, please check the file format.")

    input("按任意键退出...")        