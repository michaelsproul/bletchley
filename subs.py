"""Useful tools for solving substitution ciphers."""

import random

lc_letters = [chr(ord("a") + i) for i in range(26)]
uc_letters = [chr(ord("A") + i) for i in range(26)]
letters = [l for l in lc_letters]
letters.extend(uc_letters)

def caesar(text, shift=0):
	"Perform a Caesar shift on a given piece of text."
	shifted = ""
	for c in text:
		if c not in letters:
			shifted += c
			continue
		elif c.isupper():
			C = ord(c) - ord("A") + shift
			C = (C % 26) + ord("a")
		elif c.islower():		
			C = ord(c) - ord("a") + shift
			C = (C % 26) + ord("A")
		C = chr(C)
		shifted += C
	return shifted

def mono(text, key):
	"Substitute each letter from the text with a match from the key."
	output = ""
	for c in text:
		if c in key:
			output += key[c]
		else:
			output += c	
	return output

def random_alphabet():
	"Generate a random key."
	shuffled = [i for i in range(26)]
	for i in shuffled:
		j = random.randint(0, 25)
		temp = shuffled[i]
		shuffled[i] = shuffled[j]
		shuffled[j] = temp
	key = {uc_letters[i]: lc_letters[shuffled[i]] for i in shuffled}
	return key

def freq(ciphertext):
	"Count the frequency of each letter in the ciphertext."
	freq = {l: 0 for l in uc_letters}
	n = 0
	for c in ciphertext:
		if c in uc_letters:
			freq[c] += 1
			n += 1

	for l in freq:
		freq[l] = round(freq[l]/n, 3)
	return freq

def find_repeats(string, l=3):
	"""Find the repeated words of length l in a given string.

	Return a list of the repeated words found and the positions at which
	they appear in the string.
	"""
	words = {}
	n = len(string)
	for i in range(0, n - l + 1):
		w = string[i:i + l]
		if w in words:
			words[w].append(i)
		else:
			words[w] = [i]

	repeats = {}
	for w in words:
		if len(words[w]) > 1:
			repeats[w] = words[w]

	return repeats

def gap_distances(repeats):
	"Calculate the set of distances between repeated words."
	distances = set()
	for w in repeats:
		pos = repeats[w]
		for i in range(len(pos) - 1):
			distances.add(pos[i + 1] - pos[i])
	return distances

def vigenere(text, key, reverse=False):
	"Perform a Vigenere cipher on the given text using the key provided."
	output = ""

	# Calculate the equivalent caesar shift for each letter in the key
	key = key.lower()
	shifts = [lc_letters.index(l) for l in key]
	if reverse:
		shifts = [26 - i for i in shifts]

	# Encipher each letter according to the key shifts
	n = len(key)
	for i in range(len(text)):
		output += caesar(text[i], shifts[i % n])

	return output

def all_keys(n):
	"Generate all keys of length n."
	keys = [l for l in lc_letters]
	new_keys = []
	for i in range(n - 1):
		for key in keys:
			for l in lc_letters:
				new_keys.append(key + l)
		keys = new_keys
		new_keys = []
	
	return keys
