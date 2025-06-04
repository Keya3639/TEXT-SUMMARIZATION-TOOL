# TEXT-SUMMARIZATION-TOOL

*COMPANY* : CODTECH IT SOLUTIONS PVT.LTD

*NAME* : KEYA KARUNAMOY DAS

*INTERN ID* : CT12DN1213

*DOMAIN* : ARTIFICIAL INTELLIGENCE 

*DURATION* : 12 WEEKS 

*MENTOR* : NEELA SANTHOSH KUMAR 

##
The **Text Summarization Tool** is a Python-based application that automatically generates a concise summary of a long passage of text. Built using fundamental Natural Language Processing (NLP) techniques, the tool also performs basic topic detection by identifying the most frequently occurring significant word in the input text. It is designed to help users quickly grasp the key ideas of any document without reading it in its entirety.

## Overview

This tool uses an **extractive summarization** approach powered by the LexRank algorithm. Extractive summarization involves selecting the most important sentences from the original text without altering the content. Additionally, a custom topic detection function provides a simple indication of what the text is about.

This project is especially useful for students, researchers, professionals, or anyone who works with large volumes of textual data.

## Tools and Technologies Used

- **Python**: The programming language used for the entire project, chosen for its simplicity and extensive support for NLP tasks.
- **sumy**: A Python library that provides various summarization algorithms. In this project, the **LexRankSummarizer** is used. LexRank is an unsupervised algorithm based on graph centrality and sentence similarity.
- **PlaintextParser & Tokenizer (from sumy)**: These components help process the input text and split it into analyzable sentences.
- **re (Regular Expressions)**: Used for pattern matching and filtering meaningful words during topic detection.
- **collections.Counter**: A utility used to count the frequency of each word, assisting in identifying the main topic of the input.

## Why These Tools Were Selected

- **LexRank** is an efficient summarization algorithm that does not require any labeled training data.
- **Python** provides quick prototyping and easy syntax for beginners and experienced developers alike.
- **Built-in libraries** such as `re` and `collections` reduce the need for heavy dependencies while offering reliable performance.

## Features

- Extractive summarization using the LexRank algorithm.
- Automatic topic detection by identifying the most frequent significant word.
- Customizable number of summary sentences.
- Command-line interface to input and summarize custom text.

## Advantages

- **Easy to use** and accessible via a simple script.
- **Lightweight** and runs efficiently on any standard system without requiring GPU or large memory.
- **No training required**, as it is based on unsupervised methods.
- **Readable summaries**, since the output consists of original grammatically correct sentences.
- **Modular and extendable**, allowing easy addition of features such as file upload, GUI, or alternative algorithms.

## Limitations

- **Extractive only**: It cannot rephrase or generate new sentences; it selects from existing ones.
- **Basic topic detection**: Simply finds the most frequent long word, which may not always reflect the actual subject.
- **Limited to English** due to the configuration of the tokenizer.
- **No deep semantic understanding**: Does not analyze the actual meaning behind the text, relying on surface-level similarity.

## Real-Time Applications

- **News Summarization**: Quickly understand long news articles.
- **Academic Use**: Summarize research papers, reports, and study materials.
- **Legal and Business Documents**: Extract key points from complex or lengthy documents.
- **Customer Feedback Analysis**: Reduce thousands of reviews or feedback forms into major highlights.
- **Content Repurposing**: Help writers convert long-form articles into short summaries for social media or email newsletters.
- **Education**: Allow teachers and students to condense chapters, notes, or reading material.

## Future Enhancements

- **Abstractive summarization** using models like BERT, T5, or GPT for more intelligent output.
- **Multilingual support** to handle non-English texts.
- **File input options** for PDF, DOCX, or plain text file summarization.
- **Web-based or GUI version** for non-technical users to interact more easily.
- **API integration** for developers to embed summarization into their applications.

## Conclusion

This tool offers a reliable and simple way to summarize large text inputs, saving time and increasing productivity. It serves as a solid foundation for more advanced summarization systems and can be further developed into a fully-featured NLP application.

# OUTPUT:

![Image](https://github.com/user-attachments/assets/9f36016c-92b5-4b2f-ab67-ef8961b8d33b)

