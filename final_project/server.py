from flask import Flask, render_template, request, jsonify
from EmotionDetection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/")
def render_index_page():
    return render_template('index.html')

@app.route("/emotionDetector", methods=['POST'])
def emotion_detector_route():
    # Get the text from the request
    text_to_analyze = request.json.get('text')
    
    # Call the emotion_detector function
    result = emotion_detector(text_to_analyze)
    
    # Format the response as specified
    formatted_response = f"For the given statement, the system response is 'anger': {result['anger']}, 'disgust': {result['disgust']}, 'fear': {result['fear']}, 'joy': {result['joy']} and 'sadness': {result['sadness']}. The dominant emotion is {result['dominant_emotion']}."
    
    return jsonify({"response": formatted_response})

if __name__ == "__main__":
    app.run(host="localhost", port=5000) 