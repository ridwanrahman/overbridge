def main(s: str):
    things = {
        "(": ")",
        "[": "]",
        "{": "}"
    }
    thing_list = []
    for i in range(len(s)):
        if s[i] in things:
            thing_list.append(s[i])
        else:
            if not thing_list:
                return False
            popped_item = thing_list.pop()
            if things[popped_item] != s[i]:
                return False
    if len(thing_list)>0:
        return False
    return True

if __name__ == "__main__":
    # input = "()"
    # input = "()[]{}"
    # input = "(]"
    # input = "([])"
    # input = "([)]"
    input = "){"
    print(main(input))
