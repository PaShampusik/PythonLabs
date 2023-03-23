"""Testing of task_1"""

from Task_1 import amount_of_sentences, amount_of_nondec_sentences, average_length_of_sentence, average_length_of_word, top_K_N_grams

def test_amount_of_sentences():
    """Testing method of getting the number of sentences"""

    text = "I go home. A dog Sasha! The best one?"
    assert 3 == amount_of_sentences(text)

def test_amount_of_nondec_sentences():
    """Testing method of getting the number of non-dec sentences"""

    text = "I go home. A dog Sasha! The best one?"
    assert 2 == amount_of_nondec_sentences(text)

def test_average_length_of_sentence():
    """Testing method of getting average length of sentence"""

    text = "I go dog. A dog go! The cat?"
    assert 6 == average_length_of_sentence(text)

def test_average_length_of_word():
    """Testing method of getting average length of word"""

    text = "I go dog. A dog go! The a at?"
    assert 2 == average_length_of_word(text)

def test_top_K_N_grams():
    """Testing method of getting K_N_grams"""

    text = "I go dog. A dog go! The a cat?"
    assert ("I go ", 1) == top_K_N_grams(text, 1, 2)[0]