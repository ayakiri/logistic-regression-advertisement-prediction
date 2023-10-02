import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


# import
pd.set_option("display.max_rows", None, "display.max_columns", None)
ad_data = pd.read_csv("advertising.csv")

# analyze table
print(ad_data.head(3))
print(ad_data.info())
print(ad_data.describe())

# analyze data
sns.pairplot(ad_data, hue="Clicked on Ad", palette="husl")
plt.show()

sns.histplot(ad_data, x="Age", bins=40)
sns.jointplot(ad_data, x="Age", y="Area Income")
sns.jointplot(ad_data, x="Age", y="Daily Time Spent on Site", kind="kde")
plt.show()
