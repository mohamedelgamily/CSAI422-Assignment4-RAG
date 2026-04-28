def recall_at_k(results, answer, k):
    for r in results[:k]:
        if answer.lower() in r["text"].lower():
            return 1
    return 0

def precision_at_k(results, answer, k):
    count = 0
    for r in results[:k]:
        if answer.lower() in r["text"].lower():
            count += 1
    return count / k

def mrr(results, answer):
    for i, r in enumerate(results):
        if answer.lower() in r["text"].lower():
            return 1 / (i + 1)
    return 0