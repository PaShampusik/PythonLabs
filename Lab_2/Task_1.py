import re
import os



def text() -> str:
    """Prints the text in the file"""

    os.chdir(r"D:\src\Python_labs\Lab_2")
    f = open("text.txt", "r", encoding="utf-8")
    text = f.read()
    
    return text



def amount_of_sentences(text: str) -> int:
    """Get the amount of sentences"""

    pattern = r"(?<!\.[A-Z]{1})(?<!\s[A-Z]{1})(?<!Prof)(?<!Dr)(?<!Ms)(?<!Mss)(?<!Mr)(?<!Mrs)(\.+|\!+\?*|\?+\!*)(?=.{0,2}\n*.{0,2}[\[A-Z]{1})"
    match = re.findall(pattern, text)

    return len(match) + 1


def amount_of_nondec_sentences(text: str) -> int:
    """Get the amount of non-declarative sentences

    Declarative sentence is a sentence ending with '.' or '...' separators."""
    pattern = r"(\!+|\?+)"
    match = re.findall(pattern, text)

    return len(match)


def average_length_of_sentence(text: str) -> int:
    """Get the average legth of sentence in the text"""

    pattern = r"(?<!\.[A-Z]{1})(?<!\s[A-Z]{1})(?<!Prof)(?<!Dr)(?<!Ms)(?<!Mss)(?<!Mr)(?<!Mrs)(\.+|\!\?|\?\!|\!+|\?+|\;+)(?=\s[A-Z]+|\n|\t|\s*$|\d+)"
    match = re.split(pattern, text)
    pattern1 = r"(\"+|\s+|\.+)"
    sum = 0
    symbols = 0
    for i in match:
        if (
            i != "."
            and i != "..."
            and i != "!"
            and i != "?"
            and i != "!?"
            and i != "?!"
            and i != " "
            and i != ""            
        ):
            words = re.split(pattern1, i)
            for j in words:
                if j != "." and j != '"' and j != " " and j != "  ":
                    sum += len(j)
        else:
            symbols += 1

    return sum / (len(match) - symbols)


def average_length_of_word(text: str) -> float:
    """Get the average legth of word in the text"""

    pattern = r"([\w’']+)"
    match = re.findall(pattern, text)

    return sum(len(word) for word in match) / len(match)


def top_K_N_grams(text: str, k=10, n=4) -> dict:
    """Top-K repeated N-grams in the text"""

    pattern = r"([\w’']+)"
    match = re.findall(pattern, text)

    n_grams: dict[str, int]  = {}
    n_gram: str = ""
    for i in range (0, int(len(match) - int(n))):
        for j in range (i, i + int(n)):
            n_gram += match[j] + " "
        if n_gram in n_grams:
            n_grams[n_gram] += 1
        else:
            n_grams.update({n_gram:1})
        n_gram = ""

    result = sorted(n_grams.items(), reverse= True, key = lambda item: item[1])

    return result
