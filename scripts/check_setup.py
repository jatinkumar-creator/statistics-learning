import sys

import matplotlib
import numpy
import pandas
import scipy

print("python    :", sys.version.split()[0])
print("executable:", sys.executable)
for lib in (numpy, pandas, scipy, matplotlib):
    print(f"{lib.__name__:<11}:", lib.__version__)