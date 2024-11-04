class Endpoints:
    sentiment = "/sentiment"
    bias = "/bias"
    
class Keys:
    title = "title"

class JSON:
    page_key = "page"
    type_key = "type"
    text_key = "text"
    confidence_key = "confidence"

    sentiment_key = "sentiment"
    type_positive_value = "positive"
    type_negative_value = "negative"
    
    bias_key = "bias"
    type_left_value = "left"
    type_right_value = "right"

class Sentiment:
    pos_threshold = 0.4
    neg_threshold = -0.4
    sentiment_key = "compound"

class Bias:
    side_threshold = 0.6
    