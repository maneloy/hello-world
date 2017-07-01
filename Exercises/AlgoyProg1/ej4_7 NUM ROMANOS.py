def a_romanos(n): # http://stackoverflow.com/questions/33486183/convert-from-numbers-to-roman-notation
	conv = [[1000, 'M'], [900, 'CM'], [500, 'D'], [400, 'CD'],[ 100, 'C'], [ 90, 'XC'], [ 50, 'L'], [ 40, 'XL'], [  10, 'X'], [  9, 'IX'], [  5, 'V'], [  4, 'IV'], [   1, 'I']]
	result = ''
	for denom, roman_digit in conv:
		result += roman_digit * (n//denom)
		n %= denom
	return result

print(a_romanos(1423)) # MCDXXIII


