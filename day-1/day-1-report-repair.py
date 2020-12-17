import pandas as pd

data = pd.read_csv('day-1-data.txt', header=None)

expenses = list(data[0])

for i in expenses:
    if (2020 - i) in expenses:
        print(i*(2020-i))
        break

