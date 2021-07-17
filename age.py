driving = input('請問是否開過車:')
if driving != '有' and driving != '沒有':
	raise SystemExit	
age = input('請問你的年齡:')
age = int(age)
if driving == '有':
	if age >= 18:
		print('通過')
	else :
		print('奇怪! 你麼開過車')
elif driving == '沒有':
	if age >= 18:
		print('你可以去考駕照了')
	else :
		print ('很乖')
else:
	print('只能入有或沒有')
