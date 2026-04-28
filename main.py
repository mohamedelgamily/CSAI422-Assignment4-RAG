from dataset import load_popqa_subset
from corpus import build_corpus
from retriever import Retriever
from groq_utils import expand_query, generate_answer, reflect
from evaluation import recall_at_k, precision_at_k, mrr

def main():
    data = load_popqa_subset()
    questions = [d["question"] for d in data]
    answers = [d["answer"] for d in data]

    corpus = build_corpus(questions)
    print("Corpus size:", len(corpus))

    retriever = Retriever()
    retriever.build(corpus)

    total_recall = total_prec = total_mrr = 0

    for i, q in enumerate(questions):
        print("\n====================")
        print("Q:", q)

        # baseline
        base = retriever.search(q)

        # query expansion
        exp_q = expand_query(q)
        exp = retriever.search(exp_q)

        # hybrid
        combined = base + exp
        combined = sorted(combined, key=lambda x: x["score"], reverse=True)[:3]

        print("Retrieved:")
        for r in combined:
            print(r["id"], r["text"][:80])

        # answer
        ans = generate_answer(q, combined)
        print("Answer:", ans)

        # reflection
        refined = reflect(ans)
        print("Refined:", refined)

        # evaluation
        total_recall += recall_at_k(combined, answers[i], 3)
        total_prec += precision_at_k(combined, answers[i], 3)
        total_mrr += mrr(combined, answers[i])

    n = len(questions)
    print("\n=== METRICS ===")
    print("Recall@3:", total_recall/n)
    print("Precision@3:", total_prec/n)
    print("MRR:", total_mrr/n)

if __name__ == "__main__":
    main()