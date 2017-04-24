"""
Retrive sentences from the text that have the candidate name(s) passed
"""

import nltk

# list of words for scoring positive/negative
with open ('positive_words.txt', 'r') as f:
	pos_words = f.read().split()

with open ('negative_words.txt', 'r') as f:
	neg_words = f.read().split()


class Quote:
    """
    A quote and a positive/negative/neutral flag
    """
    def __init__(self):
        self.text = ''
        self.tone = 0

    def __str__(self):
        return self.text + ' (' + self.tone + ')'


def get_quote(text):
    """
    We use a list of positive and negative words to identify the tone.
    If positive word exists in the sentence, but not "not or no" + word, we add 1 to the score.
    If negative word exists in the sentence, but not "not or no" + word, we subtract 1 from the score.
    positive score indicates positive tone, negative score indicates negative tone and zero score indicates neutral
    """
    articles = ['a', 'an', 'the']
    negatives = ['no', 'not']
    quote = Quote()
    quote.text = text
    text_words = nltk.word_tokenize(text)
    score = 0

    for index, word in enumerate(text_words):
        if word.lower() in pos_words:
            # logic to take care of phrases like "not good" or "not a good person"
            if ((index > 0 and text_words[index-1].lower() in negatives) or
                    (index > 1 and text_words[index-1].lower() in articles and
                     text_words[index-2].lower() in negatives)):
                score -= 1          # not positive = negative
            else:
                score += 1          # postive

        elif word.lower() in neg_words:
            # logic to take care of phrases like "not bad" or "not a bad person"
            if ((index > 0 and text_words[index-1].lower() in negatives) or
                    (index > 1 and text_words[index-1].lower() in articles and
                     text_words[index-2].lower() in negatives)):
                score += 1          # not negative = positive
            else:
                score -= 1          # negative

    if score > 0:
        quote.tone = 1
    elif score < 0:
        quote.tone = -1

    return quote


def get_sentences(text, names):
    """
    Returns sentences from text that conains candidate names(s).
    names is a list of name variations of candindate like ['Hillary', 'Clinton', 'Hillary Clinton']
    or ['Donald', 'Trump', 'Donald J. Trump']
    """

    sentences1 = nltk.sent_tokenize(text)
    sentences2 = []
    for sentence in sentences1:
        if any(name in sentence.split() for name in names):
            sentences2.append(sentence)

    return sentences2

