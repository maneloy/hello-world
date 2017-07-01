def euclides(n, m):
	r = m%n
	while r != 0:		
		m = n
		n = r
		r = m%n
	return n
	
print(euclides(15, 9))
print(euclides(9, 15))
print(euclides(10, 8))
print(euclides(12, 6))
