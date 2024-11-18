import os
import time
import pandas as pd
from shared.preprocess import preprocess_data
from shared.predict import make_predictions
from shared.utils import load_model, save_predictions

INPUT_FOLDER = os.getenv("INPUT_FOLDER")
OUTPUT_FOLDER = os.getenv("OUTPUT_FOLDER")
MODEL_PATH = "./shared/models/trained_model.pkl"

def batch_predict():
    model = load_model(MODEL_PATH)
    while True:
        files = [f for f in os.listdir(INPUT_FOLDER) if f.endswith(".parquet")]
        for file in files:
            try:
                file_path = os.path.join(INPUT_FOLDER, file)
                data = pd.read_parquet(file_path)

                processed_data = preprocess_data(data)
                predictions = make_predictions(model, processed_data)

                output_file = os.path.join(OUTPUT_FOLDER, f"{os.path.splitext(file)[0]}_predictions.parquet")
                save_predictions(predictions, output_file)
                print(f"Processed: {file}")
            except Exception as e:
                print(f"Error processing {file}: {e}")
        time.sleep(5) 

if __name__ == "__main__":
    batch_predict()
