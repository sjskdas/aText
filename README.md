# Analysis of Text (aText)

aText is a Natural Language Processing (NLP) package. The package includes most fundamental aspects of deep linguistics processing:

- parsing (tokenization, stemming, POS tagging)
- named-entity extraction
- co-reference resolution
- supervised classications (NBC, kNBC, SVM, Fisher Kernel)
- unsupervised classifications (LSA, pLSA, LDA)
- sentiment and social network analyses
- text summarization at the sentence and clauses levels
- subject-verb-object triple extraction
- web-scraping and social media analyses (Facebook, Twitter)

The original package has been written in platform-independent Java with a graphical user interface and made accessible via  API to the jar file. A Python wrapper has been added to expose most of the functions to data scientists and engineers. The code in the notebook file aTextUsageExamples provides some example usage of the package aText - basic sentiment analysis, sentence-level summarization, and Naive Bayesian Classifer (NBC).

Requirements: Java 1.8 installed, packages py4j, requests, and subprocess, 400MB of space in the Python package directory.
