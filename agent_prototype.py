import json
import sys
from collections import Counter

# Tải knowledge base
with open('features.json', 'r', encoding='utf-8') as f:
    features = json.load(f)

def match_pain_point(pain_point):
    pain_tokens = set(pain_point.lower().split())
    
    results = []
    for feature in features:
        feature_terms = set()
        
        # Thêm từ khóa chính
        feature_terms.update([k.lower() for k in feature['keywords']])
        
        # Thêm pain points addressed
        for p in feature['pain_points_addressed']:
            feature_terms.update(p.lower().split())
            
        # Đếm số từ khóa phù hợp
        matches = len(pain_tokens.intersection(feature_terms))
        
        # Tính toán điểm liên quan
        relevance_score = int((matches / len(pain_tokens)) * 100)
        
        if relevance_score > 20:  # Ngưỡng để xem là phù hợp
            results.append({
                "feature_name": feature['feature_name'],
                "category": feature['category'],
                "how_it_helps": feature['how_it_helps'],
                "relevance_score": relevance_score,
                "more_info_link": feature['more_info_link']
            })
    
    # sắp xếp kết quả theo điểm liên quan
    results.sort(key=lambda x: x['relevance_score'], reverse=True)
    
    return {
        "suggested_solutions": results,
        "summary": "Các giải pháp phù hợp cho vấn đề của bạn."
    }

# Run
if __name__ == "__main__":
    try:
        input_data = json.loads(sys.stdin.read())
        output = match_pain_point(input_data['pain_point'])
        print(json.dumps(output, indent=2, ensure_ascii=False))
    except json.JSONDecodeError:
        print(json.dumps({"error": "Invalid JSON input"}, indent=2))