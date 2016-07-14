import json
from nltk.stem import WordNetLemmatizer
from string import punctuation
import codecs


bio_words = {'cell', 'specie', 'blood', 'body', 'group', 'plant', 'water', 'system', 'protein', 'membrane',
             'acid', 'organism', 'structure', 'growth', 'tion', 'molecule', 'chromosome', 'food', 'disease',
             'gene', 'tissue', 'medicine', 'amino', 'population', 'atom', 'animals', 'reaction', 'enzyme',
             'carbon', 'physiology', 'heart', 'substance', 'nerve', 'bacteria', 'electron', 'hydrogen',
             'hormone', 'muscle', 'compound', 'skin', 'embryo', 'oxygen', 'synthesis', 'result', 'immune',
             'brain', 'insect', 'human', 'ion', 'bond', 'chemistry', 'gland', 'bone', 'iron', 'oxidation',
             'family', 'source', 'complex', 'concentration', 'entity', 'united', 'mammal', 'human', 'south',
             'parent', 'pairs', 'mRNA', 'chemical', 'birds', 'organ', 'environment', 'charge', 'sequence',
             'cavity', 'reaction', 'vessel', 'earth', 'radiation', 'leaf', 'sperm', 'dioxide', 'eggs', 'nuclei',
             'flower', 'nutrients', 'head', 'drug', 'lungs', 'absorption', 'metal', 'fluid', 'phosphate', 'strand',
             'plasma', 'root', 'movement', 'metabolism', 'copper', 'adult', 'calcium', 'respiratory', 'algae',
             'kidney', 'receptor', 'fungi', 'stimulus', 'tree', 'nitrogen', 'soil', 'stem', 'sugar', 'father',
             'cytoplasm', 'neuron', 'pattern', 'copy', 'evolution', 'reptil', 'gametes', 'transfer', 'ACID',
             'sensory', 'spore', 'salt', 'fiber', 'pollen', 'tract', 'cleavage', 'allele', 'rain', 'marine',
             'fatty', 'weight', 'mutation', 'light', 'filament', 'disorder', 'habitat', 'signal', 'virus'}


def refiner(words):
    words = [w.strip(punctuation) for w in words]
    wnl = WordNetLemmatizer()
    return [w[0].lower() + w[1:] if w.capitalize() == w else w for w in map(wnl.lemmatize, words)]


bio_words = refiner(bio_words)

with codecs.open('final_result_dict.json', encoding="UTF-8") as f:
    crp = json.load(f)

with open('englishwords.txt') as f:
    words = map(str.strip, f)

new = {}
for key, value in crp.items():
    refined = set(refiner(value))
    preserved = refined.intersection(bio_words)
    value = refined.difference(words).union(preserved)
    new[key] = list(value)


with codecs.open('corpus_new_dict.json', 'w', encoding='UTF-8') as f:
    json.dump(new, f, indent=4)