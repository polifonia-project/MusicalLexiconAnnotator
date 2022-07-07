---
component-id: MusicalLexiconAnnotator
name: Music Lexicon Annotator
description: Component taking a text as input and annotating its content with word sense information according to Polifonia Lexicon.
type: Repository
release-date: 28/06/2022
release-number: v0.0.1
work-package: 
- WP4
licence: CC BY
links:
- https://github.com/polifonia-project/MusicalLexiconAnnotator
credits:
- https://github.com/roccotrip
---

# Polifonia Music Lexicon Annotator
## Description

The Polifonia Music Lexicon Annotator is a software that allows to identify musical concepts in text.
This module takes a text as input and annotates the content words in it with word sense information.
Word senses are taken from **[WordNet](https://wordnet.princeton.edu)**, employing the **[Polifonia Lexicon](https://github.com/polifonia-project/Polifonia-Lexicon)**, developed within the project and released with Deliverable 4.1, to identify if a particular word sense is related to music or not.
The disambiguation algorithm used to associate word senses with word form is based on the most frequent sense heuristic that has demonstrated to be a strong baseline for word sense disambiguation and is computed using the SemCor dataset.
The output annotation is in JSON and includes tokenization, lemmatization and part of speech tagging, word senses and a flag that indicates if a particular concept in a sentence is related to music.

## Installation

>git clone https://github.com/polifonia-project/MusicalLexiconAnnotator

> pip install -r requirements.txt

## How to use

The parameters of the model are the following:

- --input: the path to the file containing the text to disambiguate
- --output: the path of the output file
- --lang: the language of the text to annotate (in this release only English is supported)

