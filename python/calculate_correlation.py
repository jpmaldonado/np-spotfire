"""
[Exploratory] Column Correlation
October 2021
Version: 1.2.0
datascience@tibco.com

Calculates the correlation coefficients between columns of data. Multiple 
correlation methods are available which are: Pearson, Spearman and Kendall.

Inputs
----------
df : data table
    Data table containing the columns to be tested for correlation
encode_strings: Boolean
    (Optional) Whether columns of strings should be encoded to allow for correlation calculation. If False, or omitted, then string columns are ignored
    
Outputs
-------
output_corr_df : data table
    Data tabel containing all correlation scores in the format of {Column 1, 
    Column 2, Correlation Score, Correlation Method}

Packages Required
-------
pandas
scikit-learn

"""

import pandas as pd
from sklearn.preprocessing import LabelEncoder

## check correlation method is valid
valid_correlation_methods = ['pearson','kendall','spearman']

correlation_method = "pearson"
if any([method == str(correlation_method).lower() for method in valid_correlation_methods]) == False:
    raise ValueError("Invalid correlation method specified. Please use one of: Pearson, Kendall or Spearman")


## Filter data table passed from Spotfire to only columns of interest based
## upon another column input i.e. from feature selection marking

## If nothing is passed in default to performing correlation on all columns
if 'selected_features' in globals() and selected_features is not None:
    if len(selected_features.unique()) >= 2:
        feature_names = selected_features.unique()
        ## filter data frame down to only columns of interest
        features_df = df.loc[:,feature_names]
    elif len(selected_features.unique()) == 0:
        features_df = df.copy()
        feature_names =  features_df.columns
    else:
        raise ValueError("Not enough features selected (" + str(len(selected_features.unique())) + " were supplied). The minimum is 2.")    
else:
    features_df = df.copy()
    feature_names =  features_df.columns
    
## Handle string columns if required
if 'encode_strings' in globals() and encode_strings is not None:
    if encode_strings == True:
            label_encoder = LabelEncoder()
            features_df = features_df.apply(lambda x: label_encoder.fit_transform(x) if x.dtype == 'object' else x)

## Check we have some columns to compare - if not, and empty data frame is returned
if len(feature_names) >= 2:
    ## run correlation
    output_corr_df = features_df.corr(method=correlation_method.lower())
    output_corr_df['Column1'] = output_corr_df.index
    output_corr_df = output_corr_df.melt(id_vars=['Column1'], var_name='Column2', value_name='Correlation Score')
    ## add in correlation method column for reference
    output_corr_df["Correlation Method"] = correlation_method
    ## remove same column comparison
    output_corr_df = output_corr_df[output_corr_df.Column1 != output_corr_df.Column2]
else: ## return empty data frame
    output_corr_df = output_corr_df.append(pd.DataFrame({"Column1": [""], 
                                            "Column2": "",
                                            "Correlation Score": 0, 
                                            "Correlation Method": correlation_method
                                            }))

# Copyright (c) 2021. TIBCO Software inc.