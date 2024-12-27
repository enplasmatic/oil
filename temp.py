import re


def is_word_in_quotes(text, word):
    # Regex pattern to match text inside single or double quotes
    pattern = r"[\"']([^\"']*?" + re.escape(word) + r"[^\"']*?)[\"']"
    return re.search(pattern, text) is not None

print(is_word_in_quotes("""using "another this care" type of care""", "this"))