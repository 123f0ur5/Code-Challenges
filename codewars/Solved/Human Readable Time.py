def make_readable(seconds):
    hour = int(seconds/3660)
    min = int(seconds/60%60)
    seconds %= 60
    ans = '{:02}:{:02}:{:02}'.format(hour, min, seconds)
    return ans

ans = make_readable(86399)
print(ans)