from ai_edge_litert.interpreter import Interpreter
from PIL import Image
import numpy as np
import io

from models.classifier_output import NSFWClassifierOutput


class NSFWJSClassifier():
    def __init__(self, model_path: str):
        self.interpreter = Interpreter(model_path=model_path)
        self.interpreter.allocate_tensors()
        self.input_details = self.interpreter.get_input_details()
        self.output_details = self.interpreter.get_output_details()

    def classify(self, bytes: bytes) -> NSFWClassifierOutput:
        # Verify that the input bytes represent a valid image
        if bytes is None or len(bytes) == 0:
            raise ValueError("Input bytes are empty")

        try:
            image = Image.open(io.BytesIO(bytes))
            image.verify()
        except Exception as e:
            raise ValueError("Invalid image data") from e

        image = Image.open(io.BytesIO(bytes)).convert("RGB")
        image = image.resize(
            (self.input_details[0]['shape'][2], self.input_details[0]['shape'][1]))

        input_tsr = np.asarray(image, dtype=np.float32)
        if len(input_tsr.shape) == 3:
            input_tsr = np.expand_dims(input_tsr, axis=0)

        input_tsr /= 255.0

        self.interpreter.set_tensor(self.input_details[0]['index'], input_tsr)
        self.interpreter.invoke()

        preds = self.interpreter.get_tensor(self.output_details[0]['index'])[0]

        output = NSFWClassifierOutput(
            *[pred.item() for pred in preds]
        )
        return output
