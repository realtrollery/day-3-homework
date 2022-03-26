dict = {}
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q",
 "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j",
 "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
while True:
    lyrics = list(input().split())
    if lyrics[0] == '-1':
        break
    for w in range(len(lyrics)):
        word = list(lyrics[w])
        while word[-1] not in letters:
            word.pop()
        wordStr = "".join(word)
        wordStr.lower()
        if wordStr not in dict:
            dict[wordStr] = 1
        else:
            dict[wordStr] += 1
for key, value in dict.items():
    print(key, ' : ', value)
