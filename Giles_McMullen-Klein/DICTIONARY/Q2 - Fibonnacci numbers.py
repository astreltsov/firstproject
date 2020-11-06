n = 20
a = 0
b = 1
#d = {}
d = dict()
for i in range(1, n+1):
    d[i] = a
    a,b = b,a+b
print(d)

# v_list = []
# f_dict = {}
# k_list = [k for k in range(1, 11)]
# a = 0
# b = 1
# for i in range(10):
#     v_list.append(a)
#     a,b = b, a + b
# print(k_list)
# print(v_list)
# for n in range(10):
#     f_dict.keys(k_list[n])
# print(f_dict)