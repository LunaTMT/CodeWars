# Kata: https://www.codewars.com/kata/5264d2b162488dc400000001/train/python
# Katau Author: xDranik
# 6kyu

def spin_words(sentence):
    words = sentence.split(' ')
    words = list(map(lambda x: x[::-1] if len(x) >= 5 else x, words))
    return ' '.join(words)


if __name__ == "__main__":
    spin_words("This sentence is a sentence")#  , "This ecnetnes is a ecnetnes")
