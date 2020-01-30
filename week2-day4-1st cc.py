def computer_hcf(x, y):
   while(y):
       x, y = y, x % y
   return x
hcf = computer_hcf(300, 400)
print("The HCF is", hcf)

