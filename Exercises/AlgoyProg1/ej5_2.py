def es_primo(n):
    if n == 0 or n == 1:
        return False
    for i in range(2, n):
        if n%i == 0:
            return False
    return True

def factores(k):
    if k == 1 or k == 0:
        print('No se puede.')
        return None
    n = 1
    while True:
        if es_primo(n) == False:
            n += 1
        else:
            if k % n == 0:
                break
            else:
                n+=1
    while k != 1:
        if k % n == 0:
            print(n)
            k = k / n
        else:
            n+=1
            while True:
                if es_primo(n) == False:
                    n += 1
                else:
                    if k % n == 0:
                        break
                    else:
                        n += 1
