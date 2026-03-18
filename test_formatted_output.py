"""Script to demonstrate formatted output from emotion_detector."""

from unittest.mock import Mock, patch

from EmotionDetection import emotion_detector


def _mock_emotion_response() -> Mock:
    """Create a deterministic mocked response containing float emotion scores."""
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "emotionPredictions": [
            {
                "emotion": {
                    "anger": 0.01,
                    "disgust": 0.02,
                    "fear": 0.03,
                    "joy": 0.92,
                    "sadness": 0.02,
                }
            }
        ]
    }
    return mock_response


print("=" * 70)
print("EMOTION DETECTION - FORMATTED OUTPUT TEST")
print("=" * 70)

print("\nTest 1: Testing emotion_detector function output format")
print("-" * 70)
with patch("EmotionDetection.emotion_detection.requests.post") as mock_post:
    mock_post.return_value = _mock_emotion_response()
    result = emotion_detector("I am glad this happened")
print(f"Result: {result}")

print("\n\nTest 2: Formatted Output Structure")
print("-" * 70)
print(f"Anger:            {result['anger']}")
print(f"Disgust:          {result['disgust']}")
print(f"Fear:             {result['fear']}")
print(f"Joy:              {result['joy']}")
print(f"Sadness:          {result['sadness']}")
print(f"Dominant Emotion: {result['dominant_emotion']}")

print("\n" + "=" * 70)
print("Output format verification: PASSED")
print("Function returns dictionary with all required keys")
print("=" * 70)
