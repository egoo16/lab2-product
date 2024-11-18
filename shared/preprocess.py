import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer

def preprocess_data(data: pd.DataFrame) -> pd.DataFrame:
    imputer = SimpleImputer(strategy="most_frequent")
    data = pd.DataFrame(imputer.fit_transform(data), columns=data.columns)

    scaler = StandardScaler()
    encoder = OneHotEncoder()
    numerical_cols = data.select_dtypes(include=["float64", "int64"]).columns
    categorical_cols = data.select_dtypes(include=["object"]).columns

    if not numerical_cols.empty:
        data[numerical_cols] = scaler.fit_transform(data[numerical_cols])
    if not categorical_cols.empty:
        encoded = encoder.fit_transform(data[categorical_cols]).toarray()
        encoded_df = pd.DataFrame(encoded, columns=encoder.get_feature_names_out(categorical_cols))
        data = pd.concat([data[numerical_cols], encoded_df], axis=1)

    return data
