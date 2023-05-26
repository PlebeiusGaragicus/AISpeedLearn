# AISpeedLearn

My intent with this project is to help teach myself how to run local AI models in a userful way

The goal of this project is to create flash cards, quizzes and other useful study material based on a given corpus of material (PDFs, etc)

# Design workflow

1. Process documents into text

2. Run AI models to process into 'study' format

3. Run self-hosted web app to study these materials

4. Profit...

# Installation and Use

`poppler-qt5` is a Linux (Unix?) utility that we will use to process the PDFs into text documents

```sh
# on linux:
sudo apt-get install poppler-qt5

# on mac:
brew install poppler-qt5
```
