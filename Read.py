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

good = []
for d in data:
    if 'good' in d:
        good.append(d)

#list comprehension快寫法
#good = [d for d in data if 'good' in d]篩選

#bad = []
#for d in data:
    #bad.append('bad' in d)
#快寫法
#bad = ['bad' in d for d in data]會顯示出True or False

print('一共有', len(good), '筆留言談到good')
print(good[0])

#文字計數
wc = {} #word_count
for d in data:
    words = d.split(' ')
    for word in words:
        if word in wc:
            wc[word] += 1
        else:
            wc[word] = 1 #新增新的key進wc字典
for word in wc:
    if wc[word] > 1000000:
        print(word, wc[word])

print(len(wc))
print(wc['Jeff'])

while True:
    word = input('請問您想查甚麼字: ')
    if word == 'q':
        break
    if word in wc:
        print(word, '出現的次數為: ', wc[word])
    else:
        print('這個字沒有出現過哦!')
print('感謝您使用本查詢功能')
