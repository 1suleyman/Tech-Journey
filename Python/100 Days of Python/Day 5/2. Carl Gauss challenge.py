# When Carl Gauss, the German mathematician, was a child. 
# At ten years old, his math teacher gave him an exercise to add all the numbers from 1 to 100. 
# The teacher likely thought this would occupy him for a while, but Gauss returned within two minutes with the answer.

# Gauss realized that if the numbers were flipped, such as 100 + 99 + 98, and compared with 1 + 2 + 3, 
# each pair sums to 101: 1 + 100 = 101, 2 + 99 = 101, 3 + 98 = 101, and so on. 
# There are 50 pairs of 101, so the answer is simply 50 multiplied by 101, which is 5050.

total_amount = 0
for number in range(1,101):
    total_amount += number
print(total_amount)
