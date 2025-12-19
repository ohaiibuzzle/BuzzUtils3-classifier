import pytest
from classifier.classifier import NSFWJSClassifier


@pytest.fixture
def classifier():
    model_path = "models/nsfw_model.tflite"
    return NSFWJSClassifier(model_path=model_path)


def test_classifier_initialization(classifier):
    assert classifier.interpreter is not None
    assert classifier.input_details is not None
    assert classifier.output_details is not None


def test_classify_valid_image(classifier):
    with open("tests/assets/test.jpg", "rb") as f:
        image_bytes = f.read()

    result = classifier.classify(image_bytes)

    assert result is not None
    assert hasattr(result, 'to_dict')
    output_dict = result.to_dict()
    print(output_dict)
    assert all(key in output_dict for key in [
               "drawings", "hentai", "neutral", "porn", "sex"])
    assert all(isinstance(value, float) for value in output_dict.values())


def test_classify_invalid_image(classifier):
    invalid_bytes = b"this is not a valid image file"

    with pytest.raises(ValueError):
        classifier.classify(invalid_bytes)


def test_classify_empty_bytes(classifier):
    empty_bytes = b""

    with pytest.raises(ValueError):
        classifier.classify(empty_bytes)
