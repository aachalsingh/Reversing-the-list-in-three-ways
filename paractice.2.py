#reversing list in 3 ways
print("Enter the no. of list one by one")
size = int(input("Enter the size of list "))

#inatilizing a blank list
myList=[]

for i in range(size):
    myList.append(int(input("Enter the list element")))

#now displaying the list
print(f"your list is {myList}")

#################################
reverse1 = myList[:]
reverse1.reverse()
print(f"first reversed list is {reverse1}")

####################################
reverse2 = myList[::-1]
print(f"second reversed list is {reverse2}")

####################################
reverse3 = myList[:]
for i in range(len(reverse3) // 2):
    reverse3[i], reverse3[len(reverse3) - i - 1] = reverse3[len(reverse3) - i - 1], reverse3[i]
    # print(f"the reversed list at i={i} is {reverse3}")

print(f"My Third reversed list of {myList} is {reverse3}")
if reverse1 == reverse2 and reverse2 == reverse3:
    print("All three methods give same result\n")






