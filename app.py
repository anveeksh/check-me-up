from flask import Flask, request, render_template, jsonify
import joblib, numpy as np
from feature_extractor import extract_url_features, features_to_vector

app = Flask(__name__)
MODEL_PATH = 'model.pkl'

# load model
model = joblib.load(MODEL_PATH)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/api/predict', methods=['POST'])
def predict():
    data = request.json or {}
    text = data.get('text','').strip()
    if not text:
        return jsonify({'error':'No URL or text provided'}), 400
    # For now, we treat input as URL; email parsing can be added later
    feat = extract_url_features(text)
    vec = np.array(features_to_vector(feat)).reshape(1,-1)
    prob = model.predict_proba(vec)[0][1] if hasattr(model, 'predict_proba') else float(model.predict(vec)[0])
    pred = int(model.predict(vec)[0])
    explanation = {
        'features': feat,
        'prediction': 'phishing' if pred==1 else 'legitimate',
        'phishing_probability': round(float(prob), 4)
    }
    return jsonify(explanation)

if __name__ == '__main__':
    app.run(debug=True)