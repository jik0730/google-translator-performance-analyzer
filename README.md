# Documentation
## Analysis Flow and Development Guide
### 1. Download Test Data of English-Korean Parallel Corpus (The data is from KAIST Semantic Web Research Center)
- Download codes
- Combine txt files
- Convert to csv file

### 2. Translate the source language (English) into Target Language (Spanish) using Google Cloud Translator

Setup
------------

### 3. Calculate RIBES score using NLTK
### 4. Find the numbers of leaves and levels of dependence parse tree using NLTK.
### 5. Quality Engineering analysis on the processed data


Setup
-------------------------------------------------------------------------------


Authentication
++++++++++++++

Authentication for this service is done via an `API Key`_. To obtain an API
Key:

1. Open the `Cloud Platform Console`_
2. Make sure that billing is enabled for your project.
3. From the **Credentials** page, create a new **API Key** or use an existing
   one for your project.

.. _API Key:
    https://developers.google.com/api-client-library/python/guide/aaa_apikeys
.. _Cloud Console: https://console.cloud.google.com/project?_

Install Dependencies
++++++++++++++++++++

#. Install `pip`_ and `virtualenv`_ if you do not already have them.

#. Create a virtualenv. Samples are compatible with Python 2.7 and 3.4+.

    .. code-block:: bash

        $ virtualenv env
        $ source env/bin/activate

#. Install the dependencies needed to run the samples.

    .. code-block:: bash

        $ pip install -r requirements.txt

.. _pip: https://pip.pypa.io/
.. _virtualenv: https://virtualenv.pypa.io/
