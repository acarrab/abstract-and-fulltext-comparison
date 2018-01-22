
import random
n = 1328035
k = 100000

with open("fullTexts_subset.txt", "w") as fout:
    with open("allFulltexts.txt", "r") as fin:
        for document in fin:
            # gives us proper chance of selecting document
            if 0 == random.randrange(0, int(n / k)) or n == k:
                fout.write(document)
                k -= 1
                if k % 10000 == 0: print("written: " + str(100000 - k))
                if k == 0: break
            n -= 1
