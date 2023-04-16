#Fibonacci sequence
'''
斐波那契数列
输入：项数n
输出：前n项
'''
import os

def fibo(num) :
    numbers=[1,1]
    for i in range(num-2) :
        numbers.append(numbers[i]+numbers[i+1])
    return numbers

answer=fibo(10)
print(answer)

if not os.path.exists('requests') :
    os.mkdir('request')

file=open('request/fibo.txt','w')

for num in answer :
    file.write(str(num)+' ')

file.close()