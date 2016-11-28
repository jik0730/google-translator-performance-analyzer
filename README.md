# Quality Engineering Term Project - Quality Evalutation of Google Translator


## Analysis Flow and Development Guide

1. Download Test Data of English-Korean Parallel Corpus (The data is from KAIST Semantic Web Research Center)
  - Download codes
  - Combine txt files
  - Convert to csv file

2. Translate the source language (English) into Target Language (Spanish) using Google Cloud Translator

3. Calculate RIBES score using NLTK

4. Find the numbers of leaves and levels of dependence parse tree using NLTK.

5. Quality Engineering analysis on the processed data


## Setup

### Authentication

Authentication for this service is done via an `API Key`. To obtain an API Key:

1. Open the `Cloud Platform Console`

2. Make sure that billing is enabled for your project.

3. From the **Credentials** page, create a new **API Key** or use an existing one for your project.

### Install Dependencies

1. Install `pip`_ and `virtualenv`_ if you do not already have them.

2. Create a virtualenv. Samples are compatible with Python 3.4+.

     > $ virtualenv -p python3 env
     
     > $ source env/bin/activate

3. Install the dependencies needed to run the samples.

     >  $ pip install -r requirements.txt



