import random
COLS = 5
ROWS = 50

output1 = open("testmatrix1.txt", "w")
output2 = open("testmatrix2.txt", "w")

def normalize(array):
	sum = 0
	for x in array:
		sum += (x * x)
	sum = sum ** 0.5
	for i in range(len(array)):
		array[i] /= sum
	return array

for i in range(ROWS):
	t = []
	torted = []
	for j in range(COLS):
		temp = random.random()
		t.append(temp)
		temp += (random.random() / 1000)
		torted.append(temp)
	t = normalize(t)
	torted = normalize(torted)
	for j in range(COLS):
		output1.write(str(t[j]))
		output1.write(' ')
		output2.write(str(torted[j]))
		output2.write(' ')
	output1.write('\n')
	output2.write('\n')

output1.close()
output2.close()