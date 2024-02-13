import matplotlib.pyplot as plt
from random import randint
from random import random
# import numpy as np

lst = []
i = 0
while i < 100000:
    # Genrating random number b/w 0 - 1 and rounding off to 1 decimal place
    x = round(random(),1)
    lst.append(x)
    i = i+1


# 2. Plot the data
plt.plot(lst, label='Head_or_Tail')

# 3. Add your labels and pretty-up the plot
plt.title('Random Toss Data')
plt.xlabel('Number of Times')
plt.ylabel('Outcome Per Toss')
plt.grid(True)
plt.figtext(0.995, 0.01, 'for test purpose',ha='right', va='bottom')
plt.legend(loc='best', framealpha=0.5,prop={'size':'small'})
plt.tight_layout(pad=2)
plt.gcf().set_size_inches(10, 4)
plt.show()

# print("outcome result is", lst)