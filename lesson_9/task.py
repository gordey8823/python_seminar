import pandas as pd
import random

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})
data.head()

print(pd.get_dummies(data, columns=['whoAmI'], drop_first=True))

print(data.map(lambda x: x == "robot"))
