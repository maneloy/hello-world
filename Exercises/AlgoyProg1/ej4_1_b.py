def es_primo(n):
    if n == 0 or n == 1:
    	return False
    for i in range(2, n):
        if n%i == 0:
            return False
    return True

i = 0
num = 0
while i < 6:
	if es_primo(num):
		num += 1
		i += 1
	else:
		num += 1

print("The sixth prime is", num)
input(".")