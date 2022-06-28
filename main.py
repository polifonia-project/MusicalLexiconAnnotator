import csv
import argparse
import spacy
from collections import Counter
from nltk.corpus import wordnet as wn
import json

def get_spacy_model(lang):
    if lang.lower() == 'en':
        try:
            nlp = spacy.load("en_core_web_lg")
        except:
            spacy.cli.download("en_core_web_lg")
            nlp = spacy.load("en_core_web_lg")
        return nlp

def get_dist():
    with open('vocabs/semcor_annotations.tsv', encoding="utf-8") as f:
        reader = csv.reader(f, delimiter='\t')
        rows = [r for r in reader]
    dist = Counter([r[1] for r in rows])
    return dist

def get_map(lang):
    with open('vocabs/'+ lang+'_map.tsv', encoding="utf-8") as f:
        reader = csv.reader(f, delimiter='\t')
        rows = [r for r in reader]
    map = dict()
    for row in rows:
        map.setdefault(row[0], dict())
        map[row[0]].setdefault('bn', [])
        map[row[0]].setdefault('wn', [])
        map[row[0]].setdefault('wn2020', [])
        map[row[0]]['bn'].append(row[1])
        for wn in row[2].strip('][').split(','):
            wn = wn.strip()
            if wn.startswith('wn2020:'):
                map[row[0]]['wn2020'].append(wn)
            if wn.startswith('wn:'):
                map[row[0]]['wn'].append(wn)
    return map

def map_pos(pos):
    if pos == 'NOUN':
        return 'n'
    if pos == 'VERB':
        return 'v'
    if pos == 'ADJ':
        return 'a'
    if pos == 'ADV':
        return 'r'

def get_offset(s, pos):
    s = str(s)
    while len(s) < 8:
        s = '0'+s
    return 'wn:'+s+pos

def get_lexicon():
    with open('vocabs/Polifonia_lexicon_v21.tsv') as f:
        reader = csv.reader(f, delimiter='\t')
        lexicon = {row[0] : [row[0]] + row[2:] for row in reader}
    return lexicon

def annotate(input, output, lang):
    annotation = {}
    map = get_map(lang)
    semcor_dist = get_dist()
    lexicon = get_lexicon()
    with open(input) as f:
        text = f.read()
    nlp = get_spacy_model(lang)
    doc = nlp(text)
    for i, token in enumerate(doc):
        annotation[i] = {}
        disambiguation = ''
        is_musical = 0
        if token.pos_ in ['NOUN', 'VERB', 'ADJ', 'ADV']:
            pos = map_pos(token.pos_)
            senses = [get_offset(s.offset(), pos) for s in wn.synsets(token.lemma_, pos)]
            dist = [semcor_dist[s] for s in senses]
            idx = dist.index(max(dist))
            disambiguation = senses[idx]
            if disambiguation in lexicon:
                is_musical = 1
        annotation[i]['form'] = token.text
        annotation[i]['lemma'] = token.lemma_
        annotation[i]['pos'] = token.pos_
        annotation[i]['wordnet_offset'] = disambiguation
        annotation[i]['is_musical'] = str(is_musical)

    with open(output, 'w') as f:
        json.dump(annotation, f, indent=4)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', type=str, default='annotations/input')
    parser.add_argument('--output', type=str, default='annotations/output')
    parser.add_argument('--lang', type=str, default='EN')

    args = parser.parse_args()
    annotate(args.input, args.output, args.lang)