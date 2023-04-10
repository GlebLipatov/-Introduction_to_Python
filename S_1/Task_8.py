def split_chocolate_bar(n, m, k):
    if k < n * m and (k % n == 0 or k % m == 0):
        print('yes')
    else:
        print('no')


n = 3
m = 2
k_1 = 4
k_2 = 1

split_chocolate_bar(n, m, k_1)
split_chocolate_bar(n, m, k_2)
