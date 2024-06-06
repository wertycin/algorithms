n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
b.sort()
l = 0
r = 2*10**9
answer = 0
def ok(x, a, b, k):
    cnt = 0
    for i in range(n):
        # a[i] - fixed
        # find count of all pairs a[i], b[j]: a[i] + b[j] <= x
        l = 0
        r = n - 1
        ans = -1
        while l <= r:
            mid = (l + r) // 2
            if b[mid] <= x - a[i]:
                l = mid + 1
                ans = mid
            else:
                r = mid - 1
        cnt += (ans + 1)
    return cnt >= k
while l <= r:
    mid = (l+r) // 2
    if ok(mid, a, b, k):
        answer = mid
        r = mid - 1
    else:
        l = mid + 1
print(answer)