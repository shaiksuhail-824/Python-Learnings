def average(array):
    l=[]
    for i in range(n):
        l.append(i)
    array=set(l)
    return sum(array)/len(array)

    
         
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)