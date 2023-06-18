import bentoml 
from pathlib import Path
from tensorflow import keras

def save_model_into_bento(model_file_path: Path) -> None:
    # Loads a keras model from disk and saves it to BentoMl """

    model = keras.models.load_model(model_file_path)
    bento_model = bentoml.keras.save_model("keras_model",model)
    print(f"Bento model tag = {bento_model.tag}") 

if __name__ == "__main__":
    save_model_into_bento(Path("model"))








