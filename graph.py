# Preliminaries
import numpy as np
import pandas as pd
from pandas import DataFrame, Series
import matplotlib.pyplot as plt
import matplotlib

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


## Quick example
# import matplotlib.pyplot as plt
# import numpy as np

# ypoints = np.array([3, 8, 1, 10, 5, 7])

# plt.plot(ypoints)
# plt.show()