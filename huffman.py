from __future__ import print_function
import collections
import heapq
import Queue

class huffman_node(object):
	def __init__(self, c = "", freq = None):
		self.char = c
		self.freq = freq
		self.left = None
		self.right = None
		self.code = None

def create_tree(str):
	aps = collections.Counter(str)
	h = []
	for key in aps: #get the value in dict
		heapq.heappush(h, (aps[key], huffman_node(key, aps[key])))
	while len(h) > 1:
		temp1 = heapq.heappop(h)
		temp2 = heapq.heappop(h)
		temp = huffman_node(freq = temp1[0] + temp2[0])
		temp.left = temp1[1]
		temp.right = temp2[1]
		heapq.heappush(h, (temp1[0] + temp2[0], temp))
	temp = heapq.heappop(h)
	root = temp[1]
	return root

def print_tree(root, str, h):
	if not root.left == None:
		print_tree(root.left, str+'0', h)	
	if not root.right == None:
		print_tree(root.right, str+'1', h)
	if root.left == None and root.right == None:
		h[root.char] = str

str = 'abcdeabcdabcaba'
root = create_tree(str)
h = {}
print_tree(root, "", h)
print (h)
for i in str:
	print (h[i], end='')
print()
