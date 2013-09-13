"""Transposition ciphers"""

def transpose(text, x):
	"Transpose a message with a matrix of width x"
	transposed = ""
	n = len(text)
	for i in range(x):
		j = 0
		while (i + j < n):
			transposed += text[i + j]
			j += x
	return transposed
