data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1 #count = count + 1的快寫法
		if count % 1000 == 0: #'%'= 求餘數,ex: 10 % 3=1, 5 % 3=2 
			print(len(data))
print('檔案讀取完成 , 總共有', len(data), '筆資料')

#每筆留言平均長度
sum_len = 0
for d in data:
	sum_len = sum_len + len(d)#亦可打 sum_len += len(d)
print('留言的平均長度為', sum_len/len(data), '個字')

new =[]
for d in data:
	if len(d) < 100:
		new.append(d)
print('一共有', len(new), '筆留言小於100字')
print(new[0])
print(new[1])
