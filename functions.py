def clean_text(text, nlp):
    doc = nlp(text)
    cleaned_doc = [token.lemma_ for token in doc if not token.is_punct and not token.is_space and token.is_alpha]
    return " ".join(cleaned_doc)