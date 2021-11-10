lst=[12,35,18,9,56,24]
n=len(lst)
s=sum(lst)
mean=s/n
print("Mean is:",mean)
lst.sort()
if n%2==0:
  mid1=lst[n//2]
  mid2=lst[n//2-1]
  median=(mid1+mid2)/2
else:
  median=lst[n//2]
print("Median is:",median)
