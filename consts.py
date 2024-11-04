class Endpoints:
    sentiment = "/sentiment"
    bias = "/bias"
    
class Keys:
    title = "title"

class JSON:
    sentiment_key = "sentiment"
    
    bias_key = "bias"
    side_key = "side"
    

class Sentiment:
    pos_threshold = 0.4
    neg_threshold = -0.4
    sentiment_key = "compound"

class Bias:
    left_threshold = 0.4
    right_threshold = 0.4
    