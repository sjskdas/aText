# Analysis of Text (aText) in Python and Java

Analytsis of Text (aText) is a Natural Language Processing (NLP) package developed over many years using machine and deep learning and symbolic AI techniques. The full aText package implements the most fundamental aspects of deep linguistics processing as listed below. Many real-world applications have been written using the functionalities of aText, including legal contract verification and documents classification, investors sentiment analysis, call center chat sentiment analysis with embedded acoustic features, semantic search for accurate documents retrieval, translation of natural language query to SQL, image captioning, and extraction of information about competitive asset managers. Patents on several proprietary algorithms implemented in the package are pending.

Machine and deep learning:
- supervised document classications (NBC, kNBC, SVM, Fisher Kernel)
- unsupervised classifications and topic modeling (LSA, pLSA, LDA)
- deep learning models based on RNN/LSTM and word2vec

Linguistics processing:
- parsing (tokenization, stemming, POS tagging)
- named-entity extraction and co-reference resolution
- subject-verb-object triple extraction

Web and social media:
- sentiment and social network analyses
- text summarization at the sentence and clauses levels
- web-scraping (e.g. Amazon and TripAdvisor) of reviews
- social media (e.g. Facebook, Twitter) and email analyses

The original package has been written in platform-independent Java with a graphical user interface. For developers, aText functionalities have been made accessible via APIs to the jar file. A Python wrapper has been added to expose most of the functions for data scientists and engineers. The code in this notebook file provides the following example basic usage of the package aText - basic sentiment analysis, document classification via Naive Bayesian Classifer (NBC), and sentence-level summarization.

INSTALLATION

- Execute "pip install atext"
- Requirements: Java 1.8 installed, packages py4j and requests, 350MB of space in the Python package directory.
- Download data files from the githb repository: https://github.com/sjskdas/aText

For any further query or to obtain the other Python functions or the full Java version of the package, please contact at atext@machineanalytics.com. For details of the popular algorithms in aText, please consult the book Computational Business Analytics by Dr. Subrata Das, published by Chapman & Hall/CRC Press, 2014.
