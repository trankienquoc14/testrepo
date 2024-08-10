#Viết một hàm thêm môttj phần tử vào một vị trí nhất định trong mảng
def them_phan_tu(arr,n,x):
    arr= arr[:n]+[x]+arr[n:]
    return arr

a = [1, 3, 4, 6, 7]
n = 2
x = 8
print("Ket qua thu đươc",them_phan_tu(a,n,x))