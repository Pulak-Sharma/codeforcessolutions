n, k, l, c, d, p, nl, np = map(int, input().split())
lime_slices = c*d
salt_toast = p//np
drink_toast = k*l//nl
toasts = min(lime_slices,salt_toast,drink_toast)//n
print(toasts)