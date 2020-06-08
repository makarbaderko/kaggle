import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('train.csv')
fig = plt.figure(figsize=(18, 6))

plt.subplot2grid((2, 3), (0, 0), colspan=2)
for x in [1, 2, 3]:
    df.Age[df.Pclass == x].plot(kind='kde')
plt.title("Class wrt Age")
plt.legend(('1st', '2nd', '3rd'))

plt.subplot2grid((3, 4), (2, 0))
df.Survived[(df.Sex == 'female') & (df.Pclass == 1)].value_counts(normalize=True).plot(kind='bar', alpha=0.5, color='#FA0000')
plt.title("Survived rich women")

plt.subplot2grid((3, 4), (2, 1))
df.Survived[(df.Sex == 'female') & (df.Pclass == 3)].value_counts(normalize=True).plot(kind='bar', alpha=0.5, color='#FA0000')
plt.title("Survived poor women")

plt.show()