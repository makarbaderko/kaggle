import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('train.csv')
fig = plt.figure(figsize=(18, 6))

'''plt.subplot2grid((2, 3), (0, 0), colspan=2)
for x in [1, 2, 3]:
    df.Age[df.Pclass == x].plot(kind='kde')
plt.title("Class wrt Age")
plt.legend(('1st', '2nd', '3rd'))'''

plt.subplot2grid((3, 4), (0, 0))
df.Survived[df.Sex == "male"].value_counts(normalize=True).plot(kind='bar', alpha=0.5)
plt.title("Survived men")

plt.subplot2grid((3, 4), (0, 1))
df.Survived[df.Sex == "female"].value_counts(normalize=True).plot(kind='bar', alpha=0.5, color='#FA0000')
plt.title("Survived women")

plt.subplot2grid((3, 4), (0, 2))
df.Sex[df.Survived == 1].value_counts(normalize=True).plot(kind='bar', alpha=0.5, color=['#FA0000', 'b'])
plt.title("Survived wrt sex")

plt.subplot2grid((3, 4), (2, 0))
df.Survived[(df.Sex == 'male') & (df.Pclass == 1)].value_counts(normalize=True).plot(kind='bar', alpha=0.5, color='#FA0000')
plt.title("Survived rich men")

plt.subplot2grid((3, 4), (2, 1))
df.Survived[(df.Sex == 'male') & (df.Pclass == 3)].value_counts(normalize=True).plot(kind='bar', alpha=0.5, color='#FA0000')
plt.title("Survived poor men")


plt.show()