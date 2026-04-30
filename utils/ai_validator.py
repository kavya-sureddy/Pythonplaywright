def validate_ui(content):
    bad_words = ["error", "exception", "fail"]
    return not any(word in content.lower() for word in bad_words)