from datasets import Dataset
from sklearn.metrics import f1_score


def doc_to_text(doc: dict) -> str:
    context = doc.get("paragraph")
    question = doc.get("question")
    choices = doc.get("choices")
    letters = [chr(65 + i) for i in range(0, len(choices))]
    letters = ", ".join(letters)
    if doc.get("paragraph") is not None:
        text = f"""주어진 맥락을 천천히 읽고, 질문에 대한 적절한 정답을 {letters} 중에 골라 알파벳 하나로 답하시오. (Read the given context, and choose the correct answer to the question from options A, B, C, or D. Respond with a single alphabet.)

맥락 (Context): {context}
질문 (Question): {question}
보기 (Options): 
"""
    else:
        text = f"""주어진 질문을 천천히 읽고, 적절한 정답을 {letters} 중에 골라 알파벳 하나로 답하시오. (Read the given Question, and choose the correct answer from options A, B, C, or D. Respond with a single alphabet.)

질문 (Question): {question}
보기 (Options):
"""
    for i, choice in enumerate(choices):
        text += f"""{chr(65 + i)}. {choice}\n"""
    text += "정답 (Answer): "
    return text


def doc_to_target(doc: dict) -> str:
    try:
        idx = doc["choices"].index(doc["answer"])
        return chr(65 + idx)
    except:
        return chr(64)


def doc_to_choice(doc: dict) -> list:
    choices = doc.get("choices")
    letters = [chr(65 + i) for i in range(0, len(choices))]
    return letters

def macro_f1_score(items):
    unzipped_list = list(zip(*items))
    golds = unzipped_list[0]
    preds = unzipped_list[1]
    fscore = f1_score(golds, preds, average="macro")
    return fscore
