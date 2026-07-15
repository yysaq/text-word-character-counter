import re

def count_english_words(line: str) -> int:
    # 匹配所有连续英文字母作为一个单词，自动过滤标点、数字、空格
    words = re.findall(r'[a-zA-Z]+', line)
    return len(words)

def count_chinese_chars(line: str) -> int:
    # 匹配所有汉字，排除标点、数字、空格、英文、特殊符号
    chinese_chars = re.findall(r'[\u4e00-\u9fa5]', line)
    return len(chinese_chars)

def count_text(file_path: str, lang: str) -> int:
    total = 0
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            if lang == 'en':
                total += count_english_words(line)
            elif lang == 'ch':
                total += count_chinese_chars(line)
    return total

if __name__ == "__main__":
    file_path = input("Enter the path of the text file: ").strip()
    language = input("Enter the language (en for English, ch for Chinese): ").strip().lower()

    if language not in ('en', 'ch'):
        print("Error: Please enter 'en' or 'ch' for language option.")
    else:
        try:
            result = count_text(file_path, language)
            if language == 'en':
                print(f"Total number of words: {result}")
            else:
                print(f"Total number of Chinese characters: {result}")
        except FileNotFoundError:
            print(f"Error: File '{file_path}' not found.")
        except UnicodeDecodeError:
            print("Error: File encoding is not UTF-8, please check the file format.")