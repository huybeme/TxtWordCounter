def removePuncts(word):
    while word[len(word) -1] == ',' or word[len(word) -1] == '!' or word[len(word) -1] == '?' or word[len(word) -1] == '.'\
            or word[len(word) -1] == ';' or word[len(word) -1] == ':'\
            or word[0] == '\'' or word[len(word) - 1] == '\''\
            or word[len(word) -1] == ')' or word[0] == '('\
            or word[len(word) -1] == '\"' or word[0] == '\"'\
            or word[len(word) -1] == '”' or word[0] == '“'\
            or word[len(word) -1] == '’' or word[0] == '‘':

        if word[len(word) -1] == ',':
            word = word.rstrip(',')
        elif word[len(word) -1] == '!':
            word = word.rstrip('!')
        elif word[len(word) -1] == '?':
            word = word.rstrip('?')
        elif word[len(word) -1] == '.':
            word = word.rstrip('.')
        elif word[len(word) -1] == ';':
            word = word.rstrip(';')
        elif word[len(word) -1] == ':':
            word = word.rstrip(':')

        elif word[len(word) -1] == ')':
            word = word.rstrip(')')
        elif word[0] == '(':
            word = word.lstrip('(')

        elif word[len(word) -1] == '\'':
            word = word.rstrip('\'')
        elif word[0] == '\'':
            word = word.lstrip('\'')

        elif word[len(word) -1] == '\"':
            word = word.rstrip('\"')
        elif word[0] == '\"':
             word = word.lstrip('\"')

        elif word[0] == '“':
            word = word.lstrip('“')
        elif word[len(word) -1] == '”':
            word = word.rstrip('”')
        elif word[0] == '‘':
            word = word.lstrip('‘')
        elif word[len(word) -1] == '’':
            word = word.rstrip('’')

        if len(word) == 0:
            break

    return word

def main():
    book = open('warandpeace.txt', 'r')

    bookLength = len(book.readlines())
    print(f"the length of war and peace is {bookLength} lines.")

    book = open('warandpeace.txt', 'r')
    wordDict = {}

    for i in range(bookLength):
        line = book.readline().split()
        for words in range(len(line)):
            if removePuncts(line[words]) in wordDict:
                value = wordDict[removePuncts(line[words])]
                wordDict[removePuncts(line[words])] = value + 1
            else:
                wordDict[removePuncts(line[words]).lower()] = 1
    print()
    print(wordDict)

    book.close()

if __name__ == '__main__':
    main()