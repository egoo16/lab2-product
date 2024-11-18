import joblib

def load_model(path):
    return joblib.load(path)

def save_predictions(predictions, path):
    import pandas as pd
    df = pd.DataFrame(predictions)
    df.to_parquet(path, index=False)
