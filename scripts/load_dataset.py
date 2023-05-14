#import pandas as pd
from IPython.display import display
def read_data():
    import pandas as pd
    data = pd.read_csv("https://raw.githubusercontent.com/wesleybeckner/"\
      "ds_for_engineers/main/data/wine_quality/winequalityN.csv")
    return data
data = read_data()
display(data.head())