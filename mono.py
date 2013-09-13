"""Useful tools for solving monoalphabetic substitution ciphers"""

import random

letters = [chr(ord("a") + i) for i in range(26)]

def caesar(plaintext, shift=0):
	"Perform a Caesar shift on a given piece of plaintext"
	ciphertext = ""
	a = "a"
	for c in plaintext:
		c = c.lower()
		if c not in letters:
			pass
		else:
			C = ord(c) - ord(a) + shift
			C = (C % 26) + ord(a)
			C = chr(C)
			ciphertext += C
	return ciphertext

def mono(plaintext, key):
	"Substitute each letter in the plain text for the one in the key (a dict)"
	ciphertext = ""
	for c in plaintext:
		ciphertext += key[c.lower()]
	return ciphertext

def random_alphabet():
	"Generate a random key"
	shuffled = [i for i in range(26)]
	for i in shuffled:
		j = random.randint(0, 25)
		temp = shuffled[i]
		shuffled[i] = shuffled[j]
		shuffled[j] = temp
	key = {letters[i]: letters[shuffled[i]] for i in shuffled}
	return key

def find_repeats(string, l=3):
	"Find the repeated words of length l in a given string"
	words = {}
	n = len(string)
	for i in range(0, n - l + 1):
		w = string[i:i + l]
		if w in words:
			words[w] += 1
		else:
			words[w] = 1

	repeats = {}
	for w in words:
		if words[w] > 1:
			repeats[w] = words[w]

	return repeats

def freq(ciphertext):
	"Count the frequency of each letter in the ciphertext"
	freq = {l: 0 for l in letters}
	for c in ciphertext.lower():
		if c not in letters:
			continue
		freq[c] += 1
	return freq
