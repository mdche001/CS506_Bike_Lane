import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("Commonwealth_Connect_Bike_Lane_Obstruction_Heat_Map.csv")
pd.options.display.max_columns = df.shape[1]
print(df.describe())
print(df.shape)
df['type breakdown'] = 'others'
print(df.head())

car = ['car','vehicle','park','truck','SUV','bus','shuttle','mercedes','driver','delivery','taxi']
tree = ['tree','branch']
uber_lyft = ['uber','lyft']
garbage = ['garbage','glass','dump','Storage container','trash']
repair = ['repair','potholes','paint']
snow = ['snow']
animals = ['animal']
for i in range(df.shape[0]):
    flag = 0
    description = str(df.loc[i, 'issue_description']).lower()
    if description == 'nan':
        df.loc[i, 'type breakdown'] = 'blank'
        continue
    for ii in animals:
        if ii.lower() in description:
            df.loc[i, 'type breakdown'] = 'animals'
            flag = 1
            break
    if flag == 1:
        continue
    for ii in snow:
        if ii.lower() in description:
            df.loc[i, 'type breakdown'] = 'snow'
            flag = 1
            break
    if flag == 1:
        continue
    for ii in garbage:
        if ii.lower() in description:
            df.loc[i, 'type breakdown'] = 'garbage'
            flag = 1
            break
    if flag == 1:
        continue
    for ii in repair:
        if ii.lower() in description:
            df.loc[i, 'type breakdown'] = 'repair'
            flag = 1
            break
    if flag == 1:
        continue
    for ii in tree:
        if ii.lower() in description:
            df.loc[i, 'type breakdown'] = 'tree'
            flag = 1
            break
    if flag == 1:
        continue
    for ii in uber_lyft:
        if ii.lower() in description:
            df.loc[i, 'type breakdown'] = 'uber/lyft'
            flag = 1
            break
    if flag == 1:
        continue
    for ii in car:
        if ii.lower() in description:
            df.loc[i, 'type breakdown'] = 'illegal parking'
            flag = 1
            break
    if flag == 1:
        continue
title = df["type breakdown"]
print(title.unique())
title_dic = {}
data = []

for i in title:
    if i in title_dic:
        title_dic[i] += 1
    else:
        title_dic[i] = 1
print(sorted(title_dic.items(), key=lambda item: item[1]))

data.append(title_dic['snow'])
data.append(title_dic['repair'])
data.append(title_dic['garbage'])
data.append(title_dic['uber/lyft'])
data.append(title_dic['tree'])
data.append(title_dic['blank'])
data.append(title_dic['others'])
data.append(title_dic['illegal parking'])

print(data)
plt.figure(figsize=(10,6))
plt.xlabel('Classes',fontsize=14)
plt.ylabel('Number',fontsize=14)
classes = ['Snow','Repair','Garbage','uber/lyft','Tree','Blank','Others','Illegal parking']
for a,b in zip(classes,data):
    plt.text(a, b+0.1, '%.0f' % b, ha='center', va= 'bottom',fontsize=11)
plt.bar(classes, data,align='center', alpha=0.5)
plt.show()
