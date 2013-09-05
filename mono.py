"""Monoalphabetic substitution ciphers"""

letters = [chr(ord("a") + i) for i in range(26)]
letters.extend([chr(ord("A") + i) for i in range(26)])

def caesar(plaintext, shift=0):
	"Perform a Caesar shift on a given piece of plaintext"
	ciphertext = ""
	for c in plaintext:
		if c not in letters:
			ciphertext += c
		else:
			if c.islower():
				a = "a"
				z = "z"
			else:
				a = "A"
				z = "Z"

			C = ord(c) + shift
			if C > ord(z):
				C = ord(a) + C % (ord(z) + 1)
			C = chr(C)
			ciphertext += C
	return ciphertext
