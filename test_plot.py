import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

print("Starting plot test...", flush=True)
data = {'x': [1, 2, 3], 'y': [4, 5, 6]}
df = pd.DataFrame(data)
print("DataFrame created", flush=True)

plt.figure()
sns.scatterplot(data=df, x='x', y='y')
print("Plot created", flush=True)

plt.savefig('test_plot.png')
print("Plot saved", flush=True)
