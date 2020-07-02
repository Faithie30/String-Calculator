import re

def add(strng):
    
    strng_lst = []
    neg_strng_lst = []

    if len(strng) == 0:
        return 0

       
    for ech_lttr in re.findall(r"-?\d+", strng):
        try:
            if int(ech_lttr) >= 1000:
                ech_lttr = 0
            if int(ech_lttr) < 0:
                neg_strng_lst.append(ech_lttr)
            strng_lst.append(int(ech_lttr))
        except:
            continue
            
    if len(neg_strng_lst) > 0:
        raise Exception('negatives not allowed: {}'.format(neg_strng_lst))

    return sum(strng_lst)