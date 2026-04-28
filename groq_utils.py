from groq import Groq

client = Groq(api_key="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")

def expand_query(q):
    prompt = f"""
Convert this into a short keyword search query.
No explanation.

Question: {q}
"""
    res = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}]
    )
    return res.choices[0].message.content.strip()

def generate_answer(q, docs):
    context = "\n".join([f"{d['id']}: {d['text'][:200]}" for d in docs])

    prompt = f"""
Answer using ONLY the context.
Cite like [P0].

Question: {q}
Context:
{context}
"""
    res = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}]
    )
    return res.choices[0].message.content

def reflect(answer):
    prompt = f"""
Check if this answer is grounded in evidence.
If weak, improve it.

Answer:
{answer}
"""
    res = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}]
    )
    return res.choices[0].message.content