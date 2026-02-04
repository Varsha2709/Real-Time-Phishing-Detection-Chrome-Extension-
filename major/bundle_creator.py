# bundle_creator.py
import joblib, os, argparse, json

def make_bundle(tfidf_path, numeric_path, model_path, out_path):
    tfv = joblib.load(tfidf_path)
    num_cols = joblib.load(numeric_path)
    model = joblib.load(model_path)
    bundle = {"tfidf": tfv, "numeric_cols": num_cols, "model": model}
    joblib.dump(bundle, out_path)
    print("Saved bundle to", out_path)

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 5:
        print("Usage: python bundle_creator.py tfidf_vectorizer.joblib numeric_columns.joblib randomforest_model.joblib phishing_model_bundle.joblib")
    else:
        make_bundle(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
