nm=int(input())
sum = 0
temp = nm
while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp //= 10
if nm == sum:
   print("yes")
else:
   print("no")
