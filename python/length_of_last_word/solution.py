def length_last_word(word: str) -> int:
    return len(word.split()[-1])



if __name__ == "__main__":
    # word = "hello world"
    # word = "   fly me   to   the moon  "
    word = "luffy is still joyboy"
    print(length_last_word(word))
