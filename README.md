#Real-Time Phishing Detection Chrome Extension
A Machine Learning–powered Chrome extension that detects phishing websites in real time and displays a confidence probability. This project focuses on web security, applied machine learning, and browser extension development—ideal for students, developers, and cybersecurity enthusiasts.

#Features
✅ Real-Time Website Analysis  
Monitors the currently visited website and analyzes it instantly without interrupting browsing.

✅ Phishing Detection  
Classifies websites as phishing or legitimate using trained Machine Learning models.

✅ Probability-Based Output  
Displays the phishing probability score to help users make informed decisions.

✅ Machine Learning Pipeline  
Implements feature extraction using URL and text-based features with TF-IDF.

✅ Model Optimization  
Initially built using Logistic Regression and later optimized using Random Forest for better accuracy and robustness.

✅ Lightweight Chrome Extension  
Fast, efficient, and runs entirely during browsing sessions.



📁 Directory Structure
PhishShield/
├── major/                     # ML models, dataset, and training scripts (Backend)
│   ├── dataset_phishing.csv
│   ├── train_phish.py
│   ├── bundle_creator.py
│   ├── randomforest_model.joblib
│   ├── logistic_model.joblib
│   └── phishing_model_bundle.joblib
│
├── PhishShield_Extension/     # Chrome extension source code
│   ├── manifest.json
│   ├── background.js
│   ├── contentScript.js
│   ├── popup.html
│   ├── popup.css
│   └── popup.js
│
└── README.md




✅ Step-by-Step System Flow
1. Capture active website URL
2. Extract URL and webpage features
3. Apply trained ML model for prediction
4. Display phishing status and probability

   
#Requirements:
Python 3.x  
Google Chrome Browser  
   


▶️ Run the Project
 *Run the Backend:
   In the folder major run:
   1. Install Required Dependencies:
         pip install -r requirements.txt
         pip install flask scikit-learn joblib pandas numpy
      
   2. python -m uvicorn server:app --reload   (runs the server)

 *Load the Chrome extension manually:
  1. Open chrome://extensions/
  2. Enable Developer Mode
  3. Click Load unpacked
  4. Select the PhishShield_Extension folder

The extension will start detecting phishing websites in real time.

✅ Model Pipeline Overview
We modularized the Machine Learning workflow into the following stages:

- Feature Extraction (URL & text-based)
- TF-IDF Vectorization
- Model Training (Logistic Regression → Random Forest)
- Model Bundling for deployment
- Real-time inference via Chrome extension


✅ Educational Use
This project is ideal for:

Machine Learning projects
Cybersecurity and phishing detection studies
Browser extension development
Understanding real-time ML inference systems
Research on web security automation
