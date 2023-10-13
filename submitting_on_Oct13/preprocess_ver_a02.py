"""


conda activate P10A


ver=a01
python ./preprocess_ver_${ver}.py



# Target functions:
# generate_niraj_search_queries
# rank_niraj_pages_by_score


"""

import sys, json
from sentence_transformers import SentenceTransformer, util
import spacy


class GlobalHyper:
    """
    A class containing hyperparameters.
    """
    def __init__(self):
        self.sentence_model_name = 'sentence-transformers/LaBSE'
        self.spacy_model_name = "ja_ginza"
        # "xx_ent_wiki_sm"

        # Load LaBSE and other models
        self.sentence_model = SentenceTransformer(self.sentence_model_name)
        self.spacy_model = spacy.load(self.spacy_model_name)
        return

    def __str__(self):
        lex = {
                "Sentence_Transformers": self.sentence_model_name, 
                "Spacy": self.spacy_model_name, 
                }
        return json.dumps(lex, indent = 4, ensure_ascii = False)

    def preprocess(self):
        return


if __name__ == '__main__':
    hyper = GlobalHyper()
    print(hyper)



# End