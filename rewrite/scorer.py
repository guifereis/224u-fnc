def score_4class(actual, predicted):
    assert actual.shape[0] == predicted.shape[0]
    def calc_score_helper(actual, predicted):
        score = 0.0
        for actual_s, pred_s in zip(actual, predicted):
            if actual_s == pred_s:
                score += 0.25
                if actual_s != "unrelated":
                    score += 0.50
            if (actual_s != "unrelated") and (pred_s != "unrelated"):
                score += 0.25
        return score
    score = calc_score_helper(actual, predicted)
    max_score = calc_score_helper(actual, actual)
    return score, max_score