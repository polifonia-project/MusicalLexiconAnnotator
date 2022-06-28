---
component-id: MusicalLexiconAnnotator
name: Music Lexicon Annotator
description:
type:
release-date:
release-number:
work-package: 
- WP4
licence:
links:
- https://github.com/polifonia-project/MusicalLexiconAnnotator
credits:
- https://github.com/roccotrip
---

# Polifonia Music Lexicon Annotator
##Description

This module takes a text as input and annotate the content words in it with word sense information.
It uses the **[Polifonia Lexicon](https://github.com/polifonia-project/Polifonia-Lexicon)** to indicate if a particular word sense is related to music.
The annotation indicates also The output annotation is in JSON.

## Installation

> git clone https://github.com/polifonia-project/MusicalLexiconAnnotator
> pip install -r requirements.txt

## How to use

The parameters of the model are the following:

- --input: the path to the file containing the text to disambiguate
- --output: the path of the output file
- --lang: the language of the text to annotate (in this release only English is supported)

