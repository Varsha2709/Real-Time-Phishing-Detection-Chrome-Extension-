import joblib, re
from urllib.parse import urlparse

# load artifacts
tfv = joblib.load("tfidf_vectorizer.joblib")
num_cols = joblib.load("numeric_columns.joblib")   # list of numeric column names
model = joblib.load("logistic_model.joblib")       # or randomforest_model.joblib

def simple_domain(host):
    if not host: return ''
    parts = host.split('.')
    if len(parts) <= 2: return '.'.join(parts)
    return '.'.join(parts[-2:])

def url_features_for_one(u):
    parsed = urlparse(u)
    host = parsed.hostname or ''
    dom = simple_domain(host)
    return {
        'url_len': len(u),
        'host_len': len(host),
        'domain_len': len(dom),
        'subdomain_count': 0 if host=='' else max(0, len(host.split('.'))-2),
        'count_dots': u.count('.'),
        'count_hyphen': u.count('-'),
        'count_at': u.count('@'),
        'num_q': u.count('?'),
        'num_eq': u.count('='),
        'num_slash': u.count('/'),
        'num_digits': sum(ch.isdigit() for ch in u),
        'has_ip': 1 if re.search(r'http[s]?:\/\/\d+\.\d+\.\d+\.\d+', u) else 0,
        'https': 1 if u.lower().startswith('https') else 0,
        'susp_keyword': 1 if re.search(r'login|secure|account|update|verify|signin|bank|confirm|paypal|ebay', u, re.I) else 0
    }

def predict_url(u):
    num_feat = url_features_for_one(u)
    # order numeric features same as training order
    X_num = [num_feat[c] for c in num_cols]
    X_tfidf = tfv.transform([u.split('//',1)[-1]])
    import scipy.sparse as sp
    X_comb = sp.hstack([sp.csr_matrix([X_num]), X_tfidf]).tocsr()
    proba = model.predict_proba(X_comb)[0,1]
    return proba

# Example
print(predict_url("http://example.com/login"))
