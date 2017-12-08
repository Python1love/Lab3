import seaborn as sns
from diagram_friends import age_list
import matplotlib.pyplot as plt

sns.set()
ax = sns.distplot(age_list, hist=True, color="r", axlabel="Age")

plt.show()




