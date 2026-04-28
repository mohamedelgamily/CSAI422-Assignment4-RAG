import wikipedia

def build_corpus(questions):
    corpus = []

    for i, q in enumerate(questions):
        try:
            results = wikipedia.search(q)

            if not results:
                continue

            page = wikipedia.page(results[0])
            text = page.content[:1000]

            corpus.append({
                "id": f"P{i}",
                "text": text
            })

        except:
            continue


    if len(corpus) == 0:
        print("⚠️ Wikipedia failed — using fallback corpus")

        fallback = [
            "Paris is the capital of France.",
            "William Shakespeare wrote Hamlet.",
            "Jupiter is the largest planet in the solar system.",
            "Isaac Newton discovered gravity.",
            "Joe Biden is the president of the United States.",
            "Berlin is the capital of Germany.",
            "Rome is the capital of Italy.",
            "Leonardo da Vinci painted the Mona Lisa.",
            "Mercury is the smallest planet.",
            "Alexander Graham Bell invented the telephone."
        ]

        for i, text in enumerate(fallback):
            corpus.append({
                "id": f"P{i}",
                "text": text
            })

    return corpus