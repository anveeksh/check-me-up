import re
from urllib.parse import urlparse

SUSPICIOUS_KEYWORDS = ['login','verify','update','secure','bank','account','confirm','password','signin']

def extract_url_features(url: str) -> dict:
    # Basic normalization
    url = url.strip()
    if not url:
        return default_features()
    features = {}
    # length
    features['length'] = len(url)
    # has https
    features['has_https'] = 1 if url.startswith('https://') else 0
    # count of dots (subdomains)
    features['dots'] = url.count('.')
    # presence of '@' sign (rare in legit URLs)
    features['has_at'] = 1 if '@' in url else 0
    # number of suspicious keywords present
    low = url.lower()
    features['suspicious_kw_count'] = sum(1 for kw in SUSPICIOUS_KEYWORDS if kw in low)
    # ratio of digits
    digits = sum(ch.isdigit() for ch in url)
    features['digit_ratio'] = digits / max(1, len(url))
    # presence of hyphen (attackers often use hyphens)
    features['has_hyphen'] = 1 if '-' in url else 0
    # path length
    try:
        p = urlparse(url)
        path = p.path or ''
        features['path_len'] = len(path)
    except Exception:
        features['path_len'] = 0
    # NOTE: domain age / WHOIS is disabled in offline demo
    features['domain_age_days'] = 0.0
    return features

def default_features():
    return {
        'length':0,'has_https':0,'dots':0,'has_at':0,
        'suspicious_kw_count':0,'digit_ratio':0.0,'has_hyphen':0,'path_len':0,'domain_age_days':0.0
    }

def features_to_vector(feat: dict):
    # Order must match training
    return [
        feat['length'],
        feat['has_https'],
        feat['dots'],
        feat['has_at'],
        feat['suspicious_kw_count'],
        feat['digit_ratio'],
        feat['has_hyphen'],
        feat['path_len'],
        feat['domain_age_days']
    ]
