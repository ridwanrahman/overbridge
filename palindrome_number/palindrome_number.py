def main(num: int):
    return str(num) == str(num)[::-1]

if __name__ == '__main__':
    num=121
    print(main(num))
