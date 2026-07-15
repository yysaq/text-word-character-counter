
def count_words(line):
    words = line.split()
    return len(words)

def count_characters(line):
    return len(line)
def count_text(path, language):
    with open(path,'r',encoding='utf-8') as f:
        count = 0
        for line in f:
            if language == "en":
                count += count_words(line)
            elif language == "ch":
                count += count_characters(line)
    return count

if __name__ == "__main__":
    path = input("Enter the path of the text file: ")
    language = input("Enter the language of the text file (en for English, ch for Chinese): ")
    total_count = count_text(path, language)
    if language == "en":
        print(f"Total number of words in the text file: {total_count}")
    elif language == "ch":
        print(f"Total number of characters in the text file: {total_count}")