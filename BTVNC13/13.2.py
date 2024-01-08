file = "HumptyDumpty.txt"

def read_file(f):
    with open(f, 'r') as file:
        a = file.read()
        return a


def count_line(f):
    with open(f, 'r') as file:
        lines = file.readlines()
        line_count = len(lines)
        return line_count


def count_words(f):
    with open(f, 'r') as file:
        words = file.read()
        word_count = len(words.split())
        return word_count


def count_char(f):
    with open(f, 'r') as file:
        chars = file.read()
        char_count = len(chars)
        return char_count
    

print("Content of file: ",read_file(file))
print("-----Report: Lines/ Words/ Chars-----")
print("Lines:",count_line(file),"Words:",count_words(file),"Chars:",count_char(file))