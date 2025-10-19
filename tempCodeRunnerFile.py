class kelement():
    def rotate(self,arr,k):
        l=len(arr)
        k=k%l
        arr[:k]=reversed(arr[:k])
        arr[k:]=reversed(arr[k:])
        arr.reverse()
        return arr

ke=kelement()
roo=ke.rotate(arr=[1,4,2,5],k=2)
print(roo)


        