# #straight flush
# increment=0
# kartu=["2h","2s","2w","2k","3h","3s","3w","3k","4h","4s","4w","4k","5h","5s","5w","5k"
#         ,"6h","6s","6w","6k","7h","7s","7w","7k","8h","8s","8w","8k","9h","9s","9w","9k"
#         ,"10h","10s","10w","10k","Jh","Js","Jw","Jk","Qh","Qs","Qw","Qk"
#         ,"Kh","Ks","Kw","Kk","Ah","As","Aw","Ak"]
# arrtemp=[]
# for i in range(1):
#     for j in range(i,i+17,4):
#         arrtemp.append(kartu[j])
#         increment+=1
# for k in range(4):
#     for l in range(k+5,k+17,4):
#         arrtemp.append(kartu[l])
#         increment+=1
#
#
#     print(arrtemp)
#     arrtemp.clear()
# print("kombinasi", increment)


#4KRTU SAMA&1beda
# increment=0
# kartu=["2h","2s","2w","2k","3h","3s","3w","3k","4h","4s","4w","4k","5h","5s","5w","5k"
#         ,"6h","6s","6w","6k","7h","7s","7w","7k","8h","8s","8w","8k","9h","9s","9w","9k"
#         ,"10h","10s","10w","10k","Jh","Js","Jw","Jk","Qh","Qs","Qw","Qk"
#         ,"Kh","Ks","Kw","Kk","Ah","As","Aw","Ak"]
# arrtemp=[]#wadah
# for i in range(0,52,4):
#     for j in range(i,i+4):
#         arrtemp.append(kartu[j])
#     for k in range(52):
#         if(arrtemp[1][0]!=kartu[k][0]):
#             arrtemp.append(kartu[k])
#             print(arrtemp)
#             arrtemp.remove(kartu[k])
#         increment+=1
#     arrtemp.clear()
# print("KOMBINASI", increment)


kartu=["2h","3h","4h","5h","6h","7h","8h","9h","10h","Jh","Qh","Kh","Ah",
       "2w","3w","4w","5w","6w","7w","8w","9w","10w","Jw","Qw","Kw","Aw",
       "2s","3s","4s","5s","6s","7s","8s","9s","10s","Js","Qs","Ks","As",
       "2k","3k","4k","5k","6k","7k","8k","9k","10k","Jk","Qk","Kk","Ak"]
#
# kartu=["2h","2s","2w","2k",
#        "3h","3s","3w","3k",
#        "4h","4s","4w","4k",
#        "5h","5s","5w","5k",
#        "6h","6s","6w","6k",
#        "7h","7s","7w","7k",
#        "8h","8s","8w","8k",
#        "9h","9s","9w","9k",
#        "10h","10s","10w","10k",
#        "Jh","Js","Jw","Jk",
#        "Qh","Qs","Qw","Qk",
#        "Kh","Ks","Kw","Kk",
#        "Ah","As","Aw","Ak"]
arrtemp=[]
increment=0
for a in range(100):
    for i in range(9):
        for j in range(i,i+52,14):
            arrtemp.append(kartu[j])
        for k in range(i+4,i+14,14):
            arrtemp.append(kartu[k])
            increment+=1
        print(arrtemp)
        arrtemp.clear()
    for i in range(10):
        for k in range(i+12,i+14,14):
            arrtemp.append(kartu[k])
        for j in range(i,i+53,14):
            arrtemp.append(kartu[j])
        print(arrtemp)
        increment +=1
        arrtemp.clear()
    for i in range(9):
        for k in range(i+26,i+52,14):
            arrtemp.append(kartu[k])
        for j in range(i + 2, i + 35, 14):
            arrtemp.append(kartu[j])
        print(arrtemp)
        increment +=1
        arrtemp.clear()
    for i in range(9):
        for k in range(i+39,i+52,14):
            arrtemp.append(kartu[k])
        for j in range(i + 1, i + 44, 14):
            arrtemp.append(kartu[j])
        print(arrtemp)
        increment +=1
        arrtemp.clear()
    for i in range(1):
            for k in range(i+38,i+52,14):
                arrtemp.append(kartu[k])
            for j in range(i , i +52, 14):
                arrtemp.append(kartu[j])
            print(arrtemp)
            increment +=1
            arrtemp.clear()
    for i in range(1):
            for k in range(i+51,i+52,14):
                arrtemp.append(kartu[k])
            for j in range(i , i +52, 14):
                arrtemp.append(kartu[j])
            print(arrtemp)
            increment +=1
            arrtemp.clear()
    for i in range(1):
            for k in range(i+25,i+35,14):
                arrtemp.append(kartu[k])
            for j in range(i , i +52, 14):
                arrtemp.append(kartu[j])
            print(arrtemp)
            increment +=1
            arrtemp.clear()
    for i in range(1):
            for k in range(i+12,i+14,14):
                arrtemp.append(kartu[k])
            for j in range(i , i +52, 14):
                arrtemp.append(kartu[j])
            print(arrtemp)
            increment +=1
            arrtemp.clear()
    for i in range(1):
            for k in range(i+12,i+38,14):
                arrtemp.append(kartu[k])
            for j in range(0, i +46, 14):
                arrtemp.append(kartu[j])
            print(arrtemp)
            increment +=1
            arrtemp.clear()
print("Kombinasi", increment)

#Spade, Heart, Club, Diamond
# kartu = [
#
#             "2s",            "2h",            "2c",            "2d",
#             "3s",            "3h",            "3c",            "3d",
#             "4s",            "4h",            "4c",            "4d",
#             "5s",            "5h",            "5c",            "5d",
#             "6s",            "6h",            "6c",            "6d",
#             "7s",            "7h",            "7c",            "7d",
#             "8s",            "8h",            "8c",            "8d",
#             "9s",            "9h",            "9c",            "9d",
#             "10s",           "10h",           "10c",           "10d",
#             "Js",            "Jh",            "Jc",            "Jd",
#             "Qs",            "Qh",            "Qc",            "Qd",
#             "Ks",            "Kh",            "Kc",            "Kd",
#             "As",            "Ah",            "Ac",            "Ad",
#
#         ]
# increment=0
# arrtemp=[]
# i=1
# for i in range(0,i+35,4):
#     for k in range(i,i+6,52):
#         arrtemp.append(kartu[i])
#     for j in range(i+4,i+52,52):
#         arrtemp.append(kartu[j])
#     print(arrtemp)
#     arrtemp.clear()
# increment +=1
#
#
# print("Kombinasi :" )

# kartu = [
#             "A♥",            "A♦",            "A♣",            "A♠",
#             "2♥",            "2♦",            "2♣",            "2♠",
#             "3♥",            "3♦",            "3♣",            "3♠",
#             "4♥",            "4♦",            "4♣",            "4♠",
#             "5♥",            "5♦",            "5♣",            "5♠",
#             "6♥",            "6♦",            "6♣",            "6♠",
#             "7♥",            "7♦",            "7♣",            "7♠",
#             "8♥",            "8♦",            "8♣",            "8♠",
#             "9♥",            "9♦",            "9♣",            "9♠",
#             "10♥",           "10♦",           "10♣",           "10♠",
#             "J♥",            "J♦",            "J♣",            "J♠",
#             "Q♥",            "Q♦",            "Q♣",            "Q♠",
#             "K♥",            "K♦",            "K♣",            "K♠",
#
#         ]
# ST=[]
# inc=0
# i=1
# for i in range(0,i+35,4):
#     for k in range(i, i + 6, 52): #a
#         ST.append(kartu[i])
#     for l in range(i+4, i + 52, 52): #2
#         ST.append(kartu[l])
#     for m in range(l + 4, l + 6, 52): #3
#         ST.append(kartu[m])
#     for n in range(m + 4, m + 6, 52): #4
#         ST.append(kartu[n])
#     for o in reversed(range(n+7,n+14,14)) : #5
#         ST.append(kartu[o])
#         inc+=1
#         print(ST)
#         ST.clear()
# print("Kombinsi :" ,inc)