def is_isogram(string):
    string = string.lower()
    if len([True for char in set(string) if string.count(char) > 1]) >= 1:
        return False
    return True

if __name__ == "__main__":
    is_isogram("aba"), False
