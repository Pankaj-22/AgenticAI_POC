## Quick example 1
# Preliminaries
import numpy as np
import pandas as pd
from pandas import DataFrame, Series
import matplotlib.pyplot as plt
import matplotlib as mpl

# Using matplotlib in a non-pythonic way
# 1. Get some (fake) data - monthly time series
x = pd.period_range('1980-01-01',periods=420, freq='M')
x = x.to_timestamp().to_pydatetime()
y = np.random.randn(len(x)).cumsum()

# 2. Plot the data
plt.plot(x, y, label='FDI')

# 3. Add your labels and pretty-up the plot
plt.title('Fake Data Index')
plt.xlabel('Date')
plt.ylabel('Index')
plt.grid(True)
plt.figtext(0.995, 0.01, 'Footnote',ha='right', va='bottom')
plt.legend(loc='best', framealpha=0.5,prop={'size':'small'})
plt.tight_layout(pad=1)
plt.gcf().set_size_inches(10, 4)

# 4. SAVE the figure
# plt.savefig('filename.png')

# 5. Finally, close the figure
# plt.close()

# Alternatively, SHOW the figure
# With IPython, follow steps 1 to 3 above then
plt.show() # Note: also closes the figure


## Quick example 2
# import matplotlib.pyplot as plt
# import numpy as np

# ypoints = np.array([3, 8, 1, 10, 5, 7])

# plt.plot(ypoints)
# plt.show()

## Quick example 3
# import numpy as np
# import matplotlib as mpl
# import matplotlib.pyplot as plt

x = np.linspace(0, 2*np.pi, 100)
y = np.cos(x)

fig, ax = plt.subplots()
ax.plot(x, y, color='green')
plt.show()



# Scatter Graph

# fig, ax = plt.subplots(figsize=(8,3))
# ax.scatter(lst1,lst2, alpha=0.5, color='orchid')
# fig.suptitle('Random Toss Data')
# fig.tight_layout(pad=2)
# ax.grid(True)
# plt.show()