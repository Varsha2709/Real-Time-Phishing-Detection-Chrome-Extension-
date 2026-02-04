
# 🛡️ Real-Time Phishing Detection Chrome Extension using Machine Learning

PhishShield is a real-time phishing detection system built as a Google Chrome extension.
It analyzes the currently visited website and classifies it as phishing or legitimate,
while displaying a confidence probability to help users make informed security decisions.

The project initially used Logistic Regression and was later optimized using a
Random Forest classifier for improved accuracy and robustness.

------------------------------------------------------------

FEATURES

- Real-time phishing website detection
- Displays phishing probability score
- Fast and lightweight Chrome extension
- Machine Learning–based classification
- Optimized Random Forest model
- Enhances web security awareness

------------------------------------------------------------

MACHINE LEARNING APPROACH

Initial Model      : Logistic Regression
Optimized Model    : Random Forest Classifier

Feature Engineering:
- URL-based features
- Text-based features using TF-IDF

Output:
- Website classification (Phishing / Legitimate)
- Confidence probability score

------------------------------------------------------------

SYSTEM WORKFLOW

1. Chrome extension captures the active website URL
2. URL and webpage features are extracted
3. Trained Random Forest model performs prediction
4. Result and probability are displayed in the extension popup

------------------------------------------------------------

TECH STACK

- Programming Languages : Python, JavaScript
- Machine Learning      : Logistic Regression, Random Forest
- Feature Extraction    : TF-IDF, URL-based features
- Backend               : Python (Flask)
- Frontend              : HTML, CSS, JavaScript
- Platform              : Google Chrome Extension

------------------------------------------------------------

<pre>
PROJECT STRUCTURE


|-- major/
|   |-- dataset_phishing.csv
|   |-- train_phish.py
|   |-- bundle_creator.py
|   |-- server.py
|   |-- randomforest_model.joblib
|   |-- logistic_model.joblib
|   |-- tfidf_vectorizer.joblib
|   |-- phishing_model_bundle.joblib
|
|-- PhishShield_Extension/
|   |-- manifest.json
|   |-- background.js
|   |-- contentScript.js
|   |-- popup.html
|   |-- popup.css
|   |-- popup.js
|
|-- README.md
</pre>



------------------------------------------------------------

HOW TO RUN THE BACKEND

Step 1: Navigate to backend folder
cd major

Step 2: Install dependencies
pip install flask scikit-learn joblib pandas numpy

Step 3: Start the backend server
python server.py



NOTE:
Keep the backend running while using the Chrome extension.

------------------------------------------------------------

HOW TO LOAD THE CHROME EXTENSION

1. Open chrome://extensions/ in Google Chrome
2. Enable Developer Mode
3. Click Load unpacked
4. Select the PhishShield_Extension folder
5. Pin the extension and start browsing

------------------------------------------------------------

FUTURE ENHANCEMENTS

- Deep learning–based phishing detection (CNN / LSTM)
- Automatic blocking of malicious websites
- Offline inference support
- Multi-attack detection (XSS, SQL Injection)
- Mobile browser compatibility

------------------------------------------------------------

EDUCATIONAL USE

This project is suitable for:
- Machine Learning projects
- Cybersecurity and phishing detection studies
- Browser extension development
- Real-time ML inference systems
- Final-year academic projects

------------------------------------------------------------

AUTHOR

Varsha Jha
Computer Science & Engineering
Interests: Machine Learning, Cybersecurity

------------------------------------------------------------

DISCLAIMER

This project is intended for educational and research purposes only
and should not replace professional security solutions.
