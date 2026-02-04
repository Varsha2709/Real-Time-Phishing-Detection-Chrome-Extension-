# server.py
# pip install fastapi uvicorn joblib scikit-learn

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import joblib, re
import numpy as np
from urllib.parse import urlparse
import scipy.sparse as sp

app = FastAPI()

# ✅ CORS — REQUIRED FOR CHROME EXTENSION
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # allow all origins (safe for project/demo)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -------- LOAD MODEL --------
BUNDLE_PATH = "phishing_model_bundle.joblib"
bundle = joblib.load(BUNDLE_PATH)

tfv = bundle["tfidf"]
numeric_cols = bundle["numeric_cols"]
model = bundle["model"]

# -------- HELPERS --------
def simple_domain(host):
    if not host:
        return ''
    parts = host.split('.')
    if len(parts) <= 2:
        return '.'.join(parts)
    return '.'.join(parts[-2:])

def url_features(u):
    parsed = urlparse(u)
    host = parsed.hostname or ''
    dom = simple_domain(host)
    return {
        'url_len': len(u),
        'host_len': len(host),
        'domain_len': len(dom),
        'subdomain_count': 0 if host == '' else max(0, len(host.split('.')) - 2),
        'count_dots': u.count('.'),
        'count_hyphen': u.count('-'),
        'count_at': u.count('@'),
        'num_q': u.count('?'),
        'num_eq': u.count('='),
        'num_slash': u.count('/'),
        'num_digits': sum(ch.isdigit() for ch in u),
        'has_ip': 1 if re.search(r'http[s]?:\/\/\d+\.\d+\.\d+\.\d+', u) else 0,
        'https': 1 if u.lower().startswith('https') else 0,
        'susp_keyword': 1 if re.search(
            r'login|secure|account|update|verify|signin|bank|confirm|paypal|ebay',
            u,
            re.I
        ) else 0
    }

# -------- INPUT SCHEMA --------
class Input(BaseModel):
    url: str
    title: str = ""
    hasPassword: bool = False
    numForms: int = 0
    hasIframe: bool = False

# -------- API --------
@app.post("/predict")
def predict(inp: Input):
    fx = url_features(inp.url)

    X_num = np.array([fx[c] for c in numeric_cols]).reshape(1, -1)
    X_tfidf = tfv.transform([inp.url.split('//', 1)[-1]])
    X_comb = sp.hstack([sp.csr_matrix(X_num), X_tfidf]).tocsr()

    proba = float(model.predict_proba(X_comb)[0, 1])

    reasons = []
    if fx['susp_keyword']:
        reasons.append("suspicious_keyword")
    if fx['has_ip']:
        reasons.append("ip_in_url")
    if fx['num_digits'] > 6:
        reasons.append("many_digits")
    if fx['url_len'] > 80:
        reasons.append("long_url")

    verdict = "phishing" if proba >= 0.7 else "benign"

    return {
        "probability": proba,
        "verdict": verdict,
        "reasons": reasons
    }
