def best_score(a_dictionary):
    if not a_dictionary:
        return None

    max_score = None
    best_key = None

    for key, value in a_dictionary.items():
        if max_score is None or value > max_score:
            max_score = value
            best_key = key

    return best_key