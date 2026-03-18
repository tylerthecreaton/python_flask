"""Flask server for web deployment of the Emotion Detector application."""

from flask import Flask, request

from EmotionDetection import emotion_detector

app = Flask("Emotion Detector")


@app.route("/emotionDetector")
def sent_analyzer() -> str:
    """Handle emotionDetector API requests from the UI."""
    text_to_analyze = request.args.get("textToAnalyze")
    response = emotion_detector(text_to_analyze)

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
    """Render application home page."""
    return app.send_static_file("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
