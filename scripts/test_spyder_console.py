# %%
print('Hello, world')

# %%
import pandas as pd
df = pd.DataFrame({'x': (1, 2, 3), 'y': (1, 4, 9)})
#print(x)

# %%
import matplotlib.pyplot as plt
plt.plot(df.x, df.y)
plt.savefig('plot.png')


# %%
import seaborn as sns
sns.scatterplot(x=df.x, y=df.y)

# %%
import plotly.express as px


# Example dataset
df = px.data.iris()

# Create a scatter plot
fig = px.scatter(df, x='sepal_width', y='sepal_length', color='species')
# Render the plot in the default web browser
fig.show(renderer='browser')
