def equilibrium_count(array):
    n = len(array)
    count=0
    for i in range(n):
        sum_left = 0
        sum_right = 0
        if i ==0:
            sum_left=array[0]
        else:
            for k in array[0:i]:
                sum_left += k
        if i == n-1:
            sum_right=array[n-1]
        else:
            for m in array[i + 1:n]:
                sum_right += m

        if sum_left==sum_right:
            count+=1
    return count

array= list(map(int,input("Enter the array elements: ").split()))
print(equilibrium_count(array))

