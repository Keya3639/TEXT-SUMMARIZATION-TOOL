# TEXT-SUMMARIZATION-TOOL

*COMPANY* : CODTECH IT SOLUTIONS PVT.LTD

*NAME* : KEYA KARUNAMOY DAS

*INTERN ID* : CT12DN1213

*DOMAIN* : ARTIFICIAL INTELLIGENCE 

*DURATION* : 12 WEEKS 

*MENTOR* : NEELA SANTHOSH KUMAR 

##

The **Text Summarization Tool** is a Python-based project that uses Natural Language Processing (NLP) to automatically summarize long texts into concise and meaningful summaries. It also features basic topic detection by identifying the most frequent significant word from the input.

## Tools and Technologies Used

- **Python**: Chosen for its simplicity and strong support for NLP tasks.
- **sumy**: A Python library offering multiple summarization techniques. This project uses the **LexRank** algorithm for extractive summarization.
- **PlaintextParser & Tokenizer (from sumy)**: Used to parse and split the input text into manageable parts.
- **re (Regular Expressions)**: Used for text cleaning and filtering during topic detection.
- **collections.Counter**: Used to identify the most frequent meaningful word to determine the topic.

## Why These Tools?

- LexRank from `sumy` is an effective, unsupervised summarization algorithm.
- Python modules like `re` and `collections` are lightweight and efficient.
- The approach is simple, extensible, and suitable for rapid prototyping or educational use.

## Features

- Extractive summarization using LexRank.
- Automatic topic detection based on word frequency.
- Command-line interface to input and summarize custom text.

## Advantages

- Lightweight and easy to run on any system.
- No training or labeled data required.
- Extracted sentences are grammatically correct and readable.
- Fast execution and easy to modify or extend.

## Limitations

- Extractive summarization only (does not generate new sentences).
- Basic topic detection may not always represent the true context.
- Limited to English input.
- No deep semantic understanding of text.

## Real-Time Applications

- Summarizing news articles for faster reading.
- Reducing the length of academic or legal documents.
- Analyzing large volumes of customer reviews or feedback.
- Helping students study large reading materials efficiently.
- Repurposing long content for blogs, newsletters, or social media.

## Future Enhancements

- Support for abstractive summarization using deep learning models (e.g., BERT, T5).
- Web or GUI-based version for non-technical users.
- Multilingual support.
- Ability to summarize documents like PDFs and Word files.

---

This tool provides a basic yet effective way to deal with information overload and can be a useful utility for students, professionals, and researchers alike.
