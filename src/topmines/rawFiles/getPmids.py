with open("qbf_abstracts.data") as realSubsets:
    with open("pmids.data", 'w') as fout:
            i = 0
            for subsetDoc in realSubsets:
                pmid = subsetDoc.split()[3]
                i += 1
                if (i % 10000 == 0): print (i)
                fout.write(pmid)
                fout.write('\n')
