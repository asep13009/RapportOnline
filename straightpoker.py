# Spade, Heart, Club, Diamond
kartu = [
            "A♥",            "A♦",            "A♣",            "A♠",
            "2♥",            "2♦",            "2♣",            "2♠",
            "3♥",            "3♦",            "3♣",            "3♠",
            "4♥",            "4♦",            "4♣",            "4♠",
            "5♥",            "5♦",            "5♣",            "5♠",
            "6♥",            "6♦",            "6♣",            "6♠",
            "7♥",            "7♦",            "7♣",            "7♠",
            "8♥",            "8♦",            "8♣",            "8♠",
            "9♥",            "9♦",            "9♣",            "9♠",
            "10♥",           "10♦",           "10♣",           "10♠",
            "J♥",            "J♦",            "J♣",            "J♠",
            "Q♥",            "Q♦",            "Q♣",            "Q♠",
            "K♥",            "K♦",            "K♣",            "K♠",

        ]
ST=[]
inc=0
i=1
print()
for i in range(0,i+35,4):
    for k in range(i, i + 6, 52): #a
        ST.append(kartu[i])
        for l in range(i+4, i + 52, 52): #2
            ST.append(kartu[l])
            for m in range(l + 4, l + 6, 52): #3
                ST.append(kartu[m])
                for n in range(m + 4, m + 6, 52): #4
                    ST.append(kartu[n])
                    for o in range(n+7,n+14,14) : #5
                        ST.append(kartu[o])
                        inc+=1
                        print(ST)
                    ST.clear()

print("Kombinsi :" ,inc)


