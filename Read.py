data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1 #count = count + 1的快寫法
		if count % 1000 == 0: #'%'= 求餘數,ex: 10 % 3=1, 5 % 3=2 
			print(len(data))
print(len(data))
print(data[0])
print('-------------------------------')
print(data[1])
