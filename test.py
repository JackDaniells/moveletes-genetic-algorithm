import pandas

dataMatrix = [
    {
        "ref": "p1",
        "venue": 2,
        "time": 660,
        "price": 4
    },
    {
        "ref": "p2",
        "venue": 0,
        "time": 570,
        "price": 2
    },
    {
        "ref": "p3",
        "venue": 2,
        "time": 300,
        "price": 6
    },
    {
        "ref": "p4",
        "venue": 2,
        "time": 0,
        "price": 4
    },
    {
        "ref": "p5",
        "venue": 0,
        "time": 90,
        "price": 1
    },
    {
        "ref": "p6",
        "venue": 2,
        "time": 390,
        "price": 3
    }
]

df = pandas.DataFrame(dataMatrix)

print(df)

def rowIndex(row):
    print(row)
    return row.name

count = 1

# df = df.sort_values('time',ascending=True)

# tc = df['time'].value_counts()
# for index, row in df.iterrows():
#     print(vc[row['time']])
#     df.at[index,'time'] = count
#     count += 1

# count = 1

column = 'price'

# vc = df.sort_values(column,ascending=True)

# print(vc)

df[column] = df[column].astype('object').astype('float64')

vc = df[column].value_counts().sort_index().astype('object')

vf = pandas.DataFrame(vc)

nc = []

counter = 1

for index, row in vf.iterrows():

    vc[index] = 0

    for i in range(counter, counter + row[column]):
        vc[index] += counter
        counter += 1

    vc[index] = float(vc[index]) / float(row[column])

for index, row in df.iterrows():

    for i, row in vf.iterrows():
        if i == df.at[index, column]:
            df.at[index, column] = vc[i]    


print(df)

