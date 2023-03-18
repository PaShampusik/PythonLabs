import re
import os


def print_text():
    """Prints the text in the file"""

    os.chdir(r"D:\src\Python_labs\Lab_2\users")
    f = open("text.txt", "r", encoding="utf-8")

    text = f.read()
    print(text)


def amount_of_sentences() -> int:
    """Get the amount of sentences"""

    os.chdir(r"D:\src\Python_labs\Lab_2")
    f = open("text.txt", "r", encoding="utf-8")

    text = f.read()
    pattern = r"(?<!\.[A-Z]{1})(?<!\s[A-Z]{1})(?<!Prof)(?<!Dr)(?<!Ms)(?<!Mss)(?<!Mr)(?<!Mrs)(\.+|\!\?|\?\!|\!+|\?+|\;+)(?=\s[A-Z]+|\n|\t|\s*$|\d+)"
    match = re.findall(pattern, text)
    return len(match)


def amount_of_nondec_sentences() -> int:
    """Get the amount of non-declarative sentences

    Declarative sentence is a sentence ending with '.' or '...' separators."""

    f = open(os.path.join(os.getcwd(), "text.txt"), "r", encoding="utf-8")

    text = f.read()
    pattern = r"(?<!\.[A-Z]{1})(?<!\s[A-Z]{1})(?<!Prof)(?<!Dr)(?<!Ms)(?<!Mss)(?<!Mr)(?<!Mrs)(\!\?|\?\!|\!+|\?+|\;+)(?=\s[A-Z]+|\n|\t|\s*$|\d+)"
    match = re.findall(pattern, text)
    return len(match)


def average_length_of_sentence() -> int:
    """Get the average legth of sentence in the text"""

    f = open(os.path.join(os.getcwd(), "text.txt"), "r", encoding="utf-8")

    text = f.read()
    pattern = r"(?<!\.[A-Z]{1})(?<!\s[A-Z]{1})(?<!Prof)(?<!Dr)(?<!Ms)(?<!Mss)(?<!Mr)(?<!Mrs)(\.+|\!\?|\?\!|\!+|\?+|\;+)(?=\s[A-Z]+|\n|\t|\s*$|\d+)"
    match = re.split(pattern, text)
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
            sum += len(i)
        else:
            symbols += 1
    return sum / (len(match) - symbols)


def average_length_of_word() -> int:
    """Get the average legth of word in the text"""

    f = open(os.path.join(os.getcwd(), "text.txt"), "r", encoding="utf-8")

    text = f.read()
    pattern = r"(\.+|\!+|\?+|\,+|\s+)\s*"
    match = re.split(pattern, text)
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
            and i != ". "
            and i != "! "
            and i != "? "
            and not i.isdigit()
        ):
            sum += len(i)
        else:
            symbols += 1
    return sum / (len(match) - symbols)


def top_K_N_grams(k=10, n=4) -> dict:
    """Top-K repeated N-grams in the text"""

    f = open(os.path.join(os.getcwd(), "text.txt"), "r", encoding="utf-8")

    text = f.read()
    pattern = r"(\**\!*\,*\.*\;*\!*\?*\**\-*\’*\”*\s+\“*|\-*\”*\**\!*\,*\.*\?*\’*\”*$|\,*\!*\.*\-+)"
    match = re.split(pattern, text)
    sum = 0
    symbols = 0
    for i in match:
        if (
            i == None
            or "." in i
            or "..." in i
            or "!" in i
            or "-" in i
            or "?" in i
            or "!?" in i
            or "?!" in i
            or "." in i
            or "!" in i
            or "?" in i
            or "," in i
            or "," in i
            or "\n" in i
            or "\t" in i
            or "\r" in i
            or "*" in i
            or "”" in i
            or "“" in i
            or ";" in i
            or ":" in i
            or " " in i
            or "  " in i
            or i.isdigit()
        ):
            match.remove(i)
        else:
            pass

    # now in MATCH we have a list of words

    n_gramms = {}
    n_gramm = ""

    for i in range(0, int(len(match)) - int(n)):

        for j in range(0, int(n)):
            n_gramm += " " + match[i + j]

        if n_gramm in n_gramms:
            n_gramms[n_gramm] += 1
        else:
            n_gramms[n_gramm] = 1
        n_gramm = ""

    sorted_n_gramms = list(sorted(n_gramms.items(), key=lambda x: x[1], reverse=True))

    return sorted_n_gramms
