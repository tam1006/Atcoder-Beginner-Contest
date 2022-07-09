N = int(input())

def iter_p_adic(p, n):
    '''
    連続して増加するp進数をリストとして返す。nはリストの長さ
    return
    ----------
    所望のp進数リストを次々返してくれるiterator
    '''
    from itertools import product
    tmp = [range(p)] * n
    return product(*tmp)

iterator = iter_p_adic(3, N)

for idxs in iterator:
    word = ''
    for idx in idxs:
        if idx == 0:
            word += 'a'
        elif idx == 1:
            word += 'b'
        else:
            word += 'c'
    
    print(word)