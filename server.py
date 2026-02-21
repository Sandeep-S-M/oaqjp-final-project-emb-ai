from flask import Flask, render_template, request, jsonify
from EmotionDetection import emotion_detector
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/emotionDetector', methods=['POST', 'GET'])
def emotionDetector():
    """SUPPORTS BOTH POST (frontend) AND GET (direct testing)"""
    # Handle POST from frontend (JSON)
    if request.method == 'POST':
        data = request.get_json()
        text = data.get('text', '')
    # Handle GET from browser/manual testing
    elif request.method == 'GET':
        text = request.args.get('textToAnalyze', '')
    # Get emotion analysis
    result = emotion_detector(text)
    response = {
        'dominant_emotion': result['dominant_emotion'],
        'scores': result['scores']
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
