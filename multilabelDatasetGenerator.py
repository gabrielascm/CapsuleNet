
"""
multilabel dataset generator

input: path to a folder with all documents and the path to a folder where all documents are structured as

folder:
--class1:
----im1
----im2
----im...
--class2:
----im5
----im4
----im2
--class3
----im1
----im2
----im5

"""


from os import listdir
import argparse
import pandas as pd
from os import path
from path import Path

parser = argparse.ArgumentParser()
parser.add_argument('-d',"--dataset1", help="<Required> unstructured dataset", required=True)
parser.add_argument('-d2','--dataset2',help="<Required> structured dataset", required=True)

args = parser.parse_args()


first_argument = args.dataset1
second_argument = args.dataset2

print(first_argument)
print(second_argument)


lisCompleta = listdir(first_argument)
lis = []
lis.append("image")
sublis = listdir(second_argument)

if ".DS_Store" in sublis:
    i = sublis.index(".DS_Store")
    sublis.pop(i)


for folder in sublis: lis.append(folder)


#df = pd.DataFrame(columns = lis)
df = pd.DataFrame()

for image in lisCompleta:
    dicts = {}
    dicts["image"] = image
    for folder in sublis:
        pathh = second_argument + "/" + folder
        with Path(pathh):
            lista = listdir(second_argument + "/" + folder)
            if image in lista:
                dicts[folder] = 1
            else:
                dicts[folder] = 0
    df = df.append(dicts, ignore_index=True)

#print(df.loc[0,:])
print(len(df.tagus.to_string(index=False)))
counts = df.tagus.value_counts()
print(counts[1])

df.to_csv("file", encoding='utf-8', index=False)



