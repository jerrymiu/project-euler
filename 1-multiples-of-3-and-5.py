threeTotal = 0
fiveTotal = 0
fifteenTotal = 0
for i in range(0, 1000, 3):
	threeTotal += i
for i in range(0, 1000, 5):
	fiveTotal += i
for i in range(0, 1000, 15):
	fifteenTotal += i
print(threeTotal  + fiveTotal - fifteenTotal)