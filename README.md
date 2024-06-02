# disease-lab
Knowledge graph informed AI for disease research

disease-lab gives researchers a framework for applying best in class knowledge graph and retrieval augmented generation techniques to their data. 
This project harnesses code from papers in a way that makes comparison on test data across different approaches possible. It offers portable Python tooling to make 
building and observing your AI experiments a breeze.

Builds upon the KG_RAG codebase and paper:
https://github.com/BaranziniLab/KG_RAG
https://arxiv.org/abs/2311.17330

---

## disease-lab package
This Python package can be installed locally. First, clone this repository:

```
$ git clone git@github.com:keppy/disease-lab.git
```

For now you will need poetry installed to build the package: https://python-poetry.org

Once Poetry is installed, you can install this package locally by running:

```
$ poetry install
```

Next, in your Python notebook or script, import the entity extractor:

```
from disease_lab.entity_extraction.disease_query import expand_disease_query
```

## Interactive mode
Currently you can run the interactive command line tool and extract diseases from a text input string

To install dependencies and start the CLI:

```
$ poetry install
$ disease-lab
```

You will be presented with a prompt `> `, enter a string containing multiple diseases to get back the entities. Note that this will not return other entities like genes or drug compounds.
