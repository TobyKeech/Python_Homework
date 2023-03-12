def latest(scores):
    return scores[-1]


def personal_best(scores):
    return max(scores)


def personal_top_three(scores):
    scores.sort(reverse = True)
    return scores[0:3]

def highest_to_lowest(scores):
        scores.sort(reverse = True)
        return scores

def top_three_in_tie(scores):
    if item in scores:
        