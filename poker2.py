kartu = ["2w",    "3w",    "4w",    "5w",    "6w",    "7w",    "8w",    "9w",    "10w",    "Jw",    "Qw",    "Kw",    "Aw",
         "2k",    "3k",    "4k",    "5k",    "6k",    "7k",    "8k",    "9k",    "10k",    "Jk",    "Qk",    "Kk",    "Ak",
         "2h",    "3h",    "4h",    "5h",    "6h",    "7h",    "8h",    "9h",    "10h",    "Jh",    "Qh",    "Kh",    "Ah",
         "2d",    "3d",    "4d",    "5d",   "6d",    "7d",    "8d",    "9d",    "10d",    "Jd",    "Qd",    "Kd",    "Ad"]
S=[]
tmp=0
for a in range (10):
    for i in range(9): #ini 2w semua
        for j in range(i,i+52,14): #iini misah
            S.append(kartu[j])
        for k in range (i+4,i+14,14):
            S.append(kartu[k])
            tmp += 1
            print(S)
            S.clear()
    for i in range(10):
            for k in range (i+12,i+14,14):
                S.append(kartu[k])
            for j in range(i,i+53,14): #iini misah
                S.append(kartu[j])
            tmp+=1
            print(S)
            S.clear()
    for i in range(10):
            for k in range (i+12,i+14,14):
                S.append(kartu[k])
            for j in range(i,i+53,14):
                S.append(kartu[j])
            tmp+=1
            print(S)
            S.clear()


print("keseluruhan : ", tmp)