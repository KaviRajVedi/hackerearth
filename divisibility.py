'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

N = int(input())
data = [int(x) for x in input().split()]


# Write your code here
ans = ""
for i in data:
    ans+=str(i)[-1]
ans = "Yes" if int(ans) % 10 == 0 else "No"
print(ans)
