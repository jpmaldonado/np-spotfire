"""
Inputs
----------
- X: Independent variables.
- y: Dependent variable / Column to predict.

Output
----------
- df: Table with projection in two dimensions of PLS, predicted PLS values and true PLS values.

"""
# https://scikit-learn.org/stable/modules/generated/sklearn.cross_decomposition.PLSRegression.html

from sklearn.cross_decomposition import PLSRegression
import pandas as pd


X = pd.DataFrame(X)
y = pd.DataFrame(y)

# WARNING: For demo purposes, empty values were replaced with zeros. 
# Ensure that your table has NO empty values before using.
X = X.fillna(0)
y = y.fillna(0)

pls = PLSRegression(n_components=2)

pls.fit(X,y)

X_transform = pls.transform(X)
df = pd.DataFrame(X_transform)
df['pred'] = pls.predict(X)
df['y'] = y