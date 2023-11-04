import sys


def decode(message: str) -> str:
    if not message:
        return ""

    result = {}
    for word in message.split():
        word = word.lower()
        if word not in result.keys():
            result[word] = 0

        result[word] += 1

    return "".join(f"{word}{count}" for word, count in result.items())


if __name__ == '__main__':
    print(decode(sys.stdin.read()))
