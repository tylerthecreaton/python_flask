"""Flask server showing blank-input error handling for Emotion Detector."""

from flask import Flask, request

from EmotionDetection import emotion_detector

app = Flask("Emotion Detector")


@app.route("/emotionDetector")
def sent_analyzer() -> str:
    """Handle API requests and return formatted emotion output."""
    text_to_analyze = request.args.get("textToAnalyze", "")

    # Explicit blank-input validation required for Task 7.
    if not text_to_analyze.strip():
        return "Invalid text! Please try again!."

    response = emotion_detector(text_to_analyze)

    if response["dominant_emotion"] is None:
        return "Invalid text! Please try again!."

    return (
        "For the given statement, the system response is "
        "'anger': {}, 'disgust': {}, 'fear': {}, 'joy': {} and 'sadness': {}. "
        "The dominant emotion is {}."
    ).format(
        response["anger"],
        response["disgust"],
        response["fear"],
        response["joy"],
        response["sadness"],
        response["dominant_emotion"],
    )


@app.route("/")
def render_index_page() -> str:
    """Render the application home page."""
    return app.send_static_file("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
