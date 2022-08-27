def rgb(r, g, b):
    ans = []
    r = max(r,0); g = max(g,0); b = max(b,0)
    r = min(r,255); g = min(g,255); b = min(b,255)

    r = hex(r); g = hex(g); b = hex(b)
    ans.append(r[2:].upper()); ans.append(g[2:].upper()); ans.append(b[2:].upper())
    ans[0] = str(ans[0]).zfill(2); ans[1] = str(ans[1]).zfill(2); ans[2] = str(ans[2]).zfill(2)
    ans = ''.join(ans)
    return ans

ans = rgb(254,2,3)

print(ans)