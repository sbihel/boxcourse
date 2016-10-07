#! /bin/env/python3

k = 31
# dic = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
comp = [0 for i in range(ord('Z'))]
comp[ord('A')] = 'T'
comp[ord('T')] = 'A'
comp[ord('G')] = 'C'
comp[ord('C')] = 'G'


def inverse_kmers(read, k):
    res = []
    for l in read:
        # res.append(dic[l])
        res.append(comp[ord(l)])
    return "".join(reversed(res))


with open("../ind_0.reads.fa") as f:
    i = 0
    for line in f:
        if i != 0:
            for j in range(100-k+1):
                kmers = line[j:j+k]
                rc = inverse_kmers(kmers, k)
                if rc < kmers:
                    print(inverse_kmers(kmers, k))
                else:
                    print(kmers)

        i = (i+1) % 2
