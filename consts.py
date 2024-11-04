class Endpoints:
    sentiment = "/sentiment"
    bias = "/bias"
    
class Keys:
    title = "title"

class JSON:
    total_key = "total"
    sentiment_key = "sentiment"
    text_key = "text"
    confidence_key = "confidence"
    type_key = "type"
    type_positive_value = "positive"
    type_negative_value = "negative"
    bias_key = "bias"
    side_key = "side"
    
    

class Sentiment:
    pos_threshold = 0.4
    neg_threshold = -0.4
    sentiment_key = "compound"

class Bias:
    left_threshold = 0.4
    right_threshold = 0.4
    