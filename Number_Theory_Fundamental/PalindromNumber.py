N=int(input("Enter Number: "))


arr=[]

while N>0:
    digit=N%10
    arr.append(digit)
    N=N//10

left=0
right=len(arr)-1
isPalindrom="Palindrome"

while left<=right:
    if arr[left] != arr[right]:
        isPalindrom="Not Palindrome"
    left+=1
    right-=1

print(isPalindrom)

