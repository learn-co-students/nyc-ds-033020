import pandas as pd
from matplotlib import pyplot as plt
plt.style.use('fivethirtyeight')

data = pd.read_csv('data.csv')
x = data['year']

bins = [1950,1960,1970,1980,1990,2000,2010,2020]
plt.hist(x,bins=bins, edgecolor='black')

plt.title('Albums by Decade')
plt.xlabel('Decade')
plt.ylabel('Number of Albums')



import pandas as pd
from matplotlib import pyplot as plt
plt.style.use('fivethirtyeight')

data = pd.read_csv('data.csv')
x = data['genre']
plt.hist(x, edgecolor='black')

plt.title("Genres on Rolling Stone's Top 500")
plt.xlabel('Genre')
plt.ylabel('Number of Albums')