#to find the max and min element of an array
class minmax():
    def maxmin(self,arr):
        max_val=arr[0]
        min_val=arr[0]
        for num in arr:
            if num>max_val:
                max_val=num
            elif num<min_val:
                min_val=num
        return[min_val,max_val]
sol=minmax()
arr=[23,4,45,6454,42]
res=sol.maxmin(arr)
print(res)

#to find the second largest
class secondlarge():
    def smax(self,arr):
        large=arr[0]
        seclarge=arr[0]
        for num in arr:
            if num>large:
                seclarge=large
                large=num
            elif num>seclarge:
                seclarge=num
        return[large,seclarge]
sel=secondlarge()
arr=[73,4,5,646531554]
ress=sel.smax(arr)
print(ress)

#finding the third largest element on O(n)
class thirdlargest():
    def thired(self,arr):
        if len(arr)<3:
            return -1
        first=second=third=float('-inf')
        for num in arr:
            if num>first:
                third=second
                second=first
                first=num
            elif num>second and num!=first:
                third=second
                second=num
            elif num>third and num!=first and num!=second:
                third=num
        return third

        
th=thirdlargest()
arr=[2,32,343,434]
reee=th.thired(arr)
print(reee)

# find the missing number in an array (and i am using set)
class missingelement:
    def miss(self,arru):
        s=set(arru)
        m=min(arru)
        n=len(arru)+1
        for i in range(m,m+n):
            if i not in s:
                return i

m=missingelement()
arru=[7,8,10]
rer=m.miss(arru)
print(rer)

#to element and travers the array
class travers():
    def trav(self,ar,x):
        for i in range(len(ar)):
            if ar[i]==x:
                return ar.index(x)
            else:
                return -1

rept=travers()
ar=[12,34,45,654]
ans=rept.trav(ar,12)
print(ans)
