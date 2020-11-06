companies =['PDS', 'PST', 'PZN', 'PB']
k = ['Open', 'High', 'Low', 'Close']
v = [[12.87, 13.23, 11.42, 13.10], [23.54, 25.76, 21.87, 22.33],
     [98.99, 102.34, 97.21, 100.065], [203.63,207.54,202.43, 205.24]]
d = {}
for i in range(len(k)):
    d[companies[i]] = dict(zip(k,v[i]))
print(d)