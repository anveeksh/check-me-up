# Train a small demo RandomForest model on synthetic features.
import random, joblib
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from feature_extractor import features_to_vector

# Create synthetic dataset
X = []
y = []
random.seed(42)
for i in range(1500):
    # generate realistic synthetic URL features
    length = random.randint(10, 100)
    has_https = random.choices([0,1], weights=[0.4,0.6])[0]
    dots = random.randint(1,5)
    has_at = random.choices([0,1], weights=[0.95,0.05])[0]
    suspicious_kw_count = random.choices([0,1,2,3], weights=[0.7,0.2,0.08,0.02])[0]
    digit_ratio = round(random.random()*0.4,3)
    has_hyphen = random.choices([0,1], weights=[0.8,0.2])[0]
    path_len = random.randint(0,50)
    domain_age = random.randint(0,5000)
    # Basic rule for label (not perfect)
    score = 0
    score += 1 if length>60 else 0
    score += 1 if has_https==0 else 0
    score += 1 if dots>3 else 0
    score += 1 if has_at==1 else 0
    score += suspicious_kw_count
    score += 1 if digit_ratio>0.15 else 0
    score += 1 if has_hyphen==1 else 0
    # label: phishing if score >=3
    label = 1 if score>=3 else 0
    X.append([length,has_https,dots,has_at,suspicious_kw_count,digit_ratio,has_hyphen,path_len,domain_age])
    y.append(label)

X = np.array(X)
y = np.array(y)

clf = RandomForestClassifier(n_estimators=120, max_depth=8, random_state=42)
clf.fit(X,y)

joblib.dump(clf, 'model.pkl')
print('Saved demo model to model.pkl')