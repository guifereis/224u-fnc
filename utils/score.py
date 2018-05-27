#Adapted from https://github.com/FakeNewsChallenge/fnc-1/blob/master/scorer.py
#Original credit - @bgalbraith

import sklearn

#LABELS = ['agree', 'disagree', 'discuss', 'unrelated']
LABELS_RELATED = ['unrelated','related']
LABELS = LABELS_RELATED
RELATED = LABELS[0:3]

def score_submission(gold_labels, test_labels):
    score = 0.0
    cm = [[0, 0],
          [0, 0]]

    for i, (g, t) in enumerate(zip(gold_labels, test_labels)):
        g_stance, t_stance = g, t
        if g_stance != "unrelated":
            g_stance = "related"
        if t_stance != "unrelated":
            t_stance = "related"
        if g_stance == t_stance:
            score += 1 # accuracy
        #if g_stance == t_stance:
        #    score += 0.25
        #    if g_stance != 'unrelated':
        #        score += 0.50
        #if g_stance in RELATED and t_stance in RELATED:
        #    score += 0.25

        cm[LABELS.index(g_stance)][LABELS.index(t_stance)] += 1
    #return None, cm # no score on binary problem
    return score, cm


def print_confusion_matrix(cm):
    lines = []
    num_cols_rows = 1+len(LABELS)
    #header = "|{:^11}|{:^11}|{:^11}|{:^11}|{:^11}|".format('', *LABELS)
    header = "|{:^11}|"*num_cols_rows
    header = header.format('', *LABELS)
    line_len = len(header)
    lines.append("-"*line_len)
    lines.append(header)
    lines.append("-"*line_len)

    hit = 0
    total = 0
    for i, row in enumerate(cm):
        hit += row[i]
        total += sum(row)
        #lines.append("|{:^11}|{:^11}|{:^11}|{:^11}|{:^11}|".format(LABELS[i],
        #                                                           *row))
        lines.append(header.format(LABELS[i], *row))
        lines.append("-"*line_len)
    print('\n'.join(lines))


def report_score(actual,predicted):
    score,cm = score_submission(actual,predicted)
    #best_score, _ = score_submission(actual,actual)
    best_score = len(actual)

    #print_confusion_matrix(cm)
    print(sklearn.metrics.confusion_matrix(actual, predicted))
    print("Score: " +str(score) + " out of " + str(best_score) + "\t("+str(score*100/best_score) + "%)")
    #return -1 # no score for binary
    return score*100/best_score


if __name__ == "__main__":
    actual = [0,0,0,0,1,1,0,3,3]
    predicted = [0,0,0,0,1,1,2,3,3]

    report_score([LABELS[e] for e in actual],[LABELS[e] for e in predicted])