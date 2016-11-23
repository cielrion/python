# おまじない
import numpy as np
import pandas as pd
pd.options.display.max_rows = 10
pd.options.display.max_columns = 15
state = np.random.RandomState(1)
import sklearn.datasets as datasets
digits = datasets.load_digits()
type(digits)
# <class 'sklearn.datasets.base.Bunch'>

# 説明変数
digits.data.shape
# (1797, 64)

# 目的変数
digits.target.shape
# (1797,)

# 目的変数を Series に変換
target = pd.Series(digits.target)
print(target.size)
# 0    0
# 1    1
# 2    2
# ...
# 1794    8
# 1795    9
# 1796    8
# Length: 1797, dtype: int64

# 説明変数を DataFrame に変換
data = pd.DataFrame(digits.data)
data
