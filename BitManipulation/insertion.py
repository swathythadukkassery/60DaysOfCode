num=int(input())
m=int(input())
i,j = map(int,input().split())
ones = ~0
left = ones<<(j+1)
# print(left)
right = ((1<<i)-1)
# print(right)
mask = left | right
nums = num & mask
m_shifted = m<<i
print(nums | m_shifted)