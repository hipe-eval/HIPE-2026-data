# HIPE-2026-data

[HIPE 2026 shared task](https://hipe-eval.github.io/HIPE-2026/) is a [CLEF 2026 Evaluation Lab](https://clef2026.clef-initiative.eu/) on the **extraction and qualification of person–place relations in multilingual historical documents**, and the third edition of the [HIPE-eval](https://hipe-eval.github.io/) shared task series.

Building on the success of [HIPE-2020](https://impresso.github.io/CLEF-HIPE-2020) and [HIPE-2022](https://impresso.github.io/CLEF-HIPE-2022), which focused on entity recognition and linking, HIPE-2026 aims to support answering the question **_Who was where, when?_** and to deepen our understanding of how people and places were connected in historical media. This will enable the reconstruction of life trajectories, the tracing of mobility patterns, and the identification of actors within local contexts.

**Table of Contents**

- [Key information](#key-information)  
- [Data](#hipe-2026-data): Information about data, including link to dataset statistics notebook.  
- [Evaluation](#prediction-and-evaluation-example): A simple example of prediction and evaluation.
- [Acknowledgements](#acknowledgements)  
- [References](#references)

## Key information

- :computer: Visit the [**website**](https://hipe-eval.github.io/HIPE-2026/) for general information on the shared task and registration.
- :notebook: Read the [**Participation Guidelines**](https://doi.org/10.5281/zenodo.17800136) for detailed information about the tasks, datasets and evaluation. [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.17800136.svg)](https://doi.org/10.5281/zenodo.17800136)
- **License**: HIPE-2026 data is released under a [CC BY-NC-SA 4.0 License](https://img.shields.io/badge/License-CC_BY--NC--SA_4.0-lightgrey.svg) [![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC_BY--NC--SA_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-sa/4.0/)
- **Where to find the data**:
  - in the [data](https://github.com/hipe-eval/HIPE-2026-data/tree/main/data/) folder of this repository
  - on Zenodo [![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.20615690-blue)](https://doi.org/10.5281/zenodo.20615690)
  - in the [GH release v1.0](https://github.com/hipe-eval/HIPE-2026-data/releases/tag/v1.0)
  
- **Release history**:
  - 12.06.2026: unmasked test data release (already available in our shared task evaluation [repository](https://github.com/hipe-eval/hipe-2026-eval/tree/main/data/reference)) and final data [release v1.0](https://github.com/hipe-eval/HIPE-2026-data/releases/tag/v1.0)
  - 05.05.2026: masked test data release
  - 22.01.2026: full training release
  - 19.12.2025: [extended data sample](https://github.com/hipe-eval/HIPE-2026-data/tree/main/data/newspapers/v1.0) release v1.0 and [sandbox](https://github.com/hipe-eval/HIPE-2026-data/tree/main/data/sandbox) release (high quality automatic annotations)
  - 04.12.2025: [data sample](https://github.com/hipe-eval/HIPE-2026-data/tree/main/data/newspapers/v1.0) + data [json schema](https://github.com/hipe-eval/HIPE-2026-data/blob/main/schemas/hipe-2026-data.schema.json)

## HIPE-2026 data

HIPE-2026 uses two evaluation domains. **Domain A** contains historical newspaper articles in German, English, and French, spanning the nineteenth and twentieth centuries, derived from the HIPE-2022 newspaper data, with manually created entity annotations and Wikidata links. **Domain B** is a surprise test set consisting of French literature and historiographical works from the sixteenth to eighteenth centuries, included to assess out-of-domain generalisation.

### Contents and preparation

**Domain A** builds on the [HIPE-2022 v2.1](https://github.com/hipe-eval/HIPE-2022-data/tree/main/data/v2.1) NE-annotated historical newspaper datasets. Primary datasets included are those that contain PERS and LOC annotations, namely: `impresso-hipe-2020`, `newseye`, `sonar`, and `letemps`. HIPE-2022 data in IOB format, containing NE mentions and Wikidata QIDs, is converted into JSON, preserving the document text and metadata, and enabling the extraction of person–place pairs.

**Domain B** entity annotations and Wikidata links come from the FreEM_NER corpus (version 6), which includes an extended and improved version of the *Presto* core corpus. The `at` relationships were annotated on top of these for this shared task. Note that Test A evaluates both `at` and `isAt` relation types; Test B evaluates only `at`.

The preparation process for both domains involved roughly the following steps:

1.  Representation transformation: convert source annotations into structured JSON.
2.  Data cleaning & filtering: merge NIL entities and remove overly long documents.
3.  Extraction of candidate person–location pairs: identify potential pairs within each document and filter.
4.  Annotation — pre-annotate with an ensemble of LLMs, then manually review and correct collaboratively.
5.  Final dataset creation: assemble dataset splits and package for release.

### Format and data representation

- HIPE-2026 data follows this [JSON schema](https://github.com/hipe-eval/HIPE-2026-data/blob/main/schemas/hipe-2026-data.schema.json).
- All documents from different primary datasets of HIPE-2022 are gathered in the same language-dependent JSON Line file.
- Information on the source document and its metadata are in the `media` property.

### Directory structure and naming convention

- Training and testing datasets consist of UTF-8 JSON Line files. There is one `.jsonl` file per language and split.
- Files are named according to this schema: `HIPE-2026-vx.x-<dataset>-<train|test>-<lg>.jsonl`.
- **Domain A** data is in `data/newspapers/`; **Domain B** data is in `data/litworks/`.
- Files ending in `_masked` are the test files as distributed during the evaluation period, with gold labels removed.
- The `sandbox/` directory contains silver (automatically annotated) data for Domain A, intended for additional pretraining or self-supervised experiments.
- Data directory is organised per HIPE release version and dataset:

  ```
  data
  ├── newspapers
  │   └── v1.0
  │       ├── HIPE-2026-v1.0-impresso-test_masked-de.jsonl
  │       ├── HIPE-2026-v1.0-impresso-test_masked-en.jsonl
  │       ├── HIPE-2026-v1.0-impresso-test_masked-fr.jsonl
  │       ├── HIPE-2026-v1.0-impresso-test-de.jsonl
  │       ├── HIPE-2026-v1.0-impresso-test-en.jsonl
  │       ├── HIPE-2026-v1.0-impresso-test-fr.jsonl
  │       ├── HIPE-2026-v1.0-impresso-train-de.jsonl
  │       ├── HIPE-2026-v1.0-impresso-train-en.jsonl
  │       └── HIPE-2026-v1.0-impresso-train-fr.jsonl
  ├── litworks
  │   └── v1.0
  │       ├── HIPE-2026-v1.0-surprise-test_masked-fr.jsonl
  │       └── HIPE-2026-v1.0-surprise-test-fr.jsonl
  └── sandbox
      ├── de-dev.jsonl
      ├── de-train.jsonl
      ├── en-dev.jsonl
      ├── en-train.jsonl
      ├── fr-dev.jsonl
      ├── fr-train.jsonl
      └── README.md
  ```

### Versioning

- HIPE-2026 releases are versioned `Major.Minor`. Version information is present in the data directory structure and data filenames.
- Each HIPE-2026 release has an equivalent git repository release, with release notes.

### Dataset statistics

In [this notebook](https://colab.research.google.com/drive/1Av87krWYI1QbQ-_q_UfrVBbKMtcInpJb#scrollTo=sNoDJI242duL) we load the training data and generate some dataset statistics.

**File overview**

The table below lists all data files with their split, annotation type, language, and document count (one document = one JSON line).

| Dataset | Split | Annotation | Lang | File | #docs |
|---------|-------|------------|------|------|------:|
| newspapers | train | gold | de | `newspapers/v1.0/HIPE-2026-v1.0-impresso-train-de.jsonl` | 34 |
| newspapers | train | gold | en | `newspapers/v1.0/HIPE-2026-v1.0-impresso-train-en.jsonl` | 35 |
| newspapers | train | gold | fr | `newspapers/v1.0/HIPE-2026-v1.0-impresso-train-fr.jsonl` | 35 |
| newspapers | test | gold | de | `newspapers/v1.0/HIPE-2026-v1.0-impresso-test-de.jsonl` | 19 |
| newspapers | test | gold | en | `newspapers/v1.0/HIPE-2026-v1.0-impresso-test-en.jsonl` | 19 |
| newspapers | test | gold | fr | `newspapers/v1.0/HIPE-2026-v1.0-impresso-test-fr.jsonl` | 19 |
| litworks | test | gold | fr | `litworks/v1.0/HIPE-2026-v1.0-surprise-test-fr.jsonl` | 30 |
| newspapers | dev | silver | de | `sandbox/de-dev.jsonl` | 32 |
| newspapers | dev | silver | en | `sandbox/en-dev.jsonl` | 17 |
| newspapers | dev | silver | fr | `sandbox/fr-dev.jsonl` | 107 |
| newspapers | train | silver | de | `sandbox/de-train.jsonl` | 88 |
| newspapers | train | silver | en | `sandbox/en-train.jsonl` | 56 |
| newspapers | train | silver | fr | `sandbox/fr-train.jsonl` | 317 |

**Note on silver vs. gold annotation overlap:** The silver train files
(`sandbox/*-train.jsonl`) contain automatic (LLM) annotations for all original silver documents, *minus* those released in the sample submissions. A subset of these documents was also manually annotated and appears in the gold train files (`newspapers/v1.0/HIPE-2026-v1.0-impresso-train-*.jsonl`). These overlapping documents are thus present in **both** the silver and gold train files, but carry different annotations (automatic vs. human). The document counts in the silver train files in this repository therefore include documents that were also manually annotated for gold train. Specifically:

| Lang | Silver train in repo | of which also in Gold train |
|------|---------------------:|----------------------------:|
| de | 88 | 24 |
| en | 56 | 33 |
| fr | 317 | 24 |

Participants who trained on both gold and silver data should be aware of this overlap.

### Data validation

To validate that your `.jsonl` files conform to the HIPE-2026 schema:

1. Create a virtual environment and install dependencies:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

2. Run the validator script directly:

   ```bash
   python scripts/check_jsonlschema.py \
      --schemafile schemas/hipe-2026-data.schema.json \
      data/newspapers/v1.0/*.jsonl data/litworks/v1.0/*.jsonl
   ```

Here, the file paths can be replaced with a path to the folder that contains your own predictions.


## Prediction and Evaluation Example

Let's pretend this gold file has no labels:

```
data/newspapers/v1.0/HIPE-2026-v1.0-impresso-train-de.jsonl
```

We first predict labels with a random baseline and save the output:

```bash
teamname=RANDOM
python scripts/dummy_predict.py \
  --input_path data/newspapers/v1.0/HIPE-2026-v1.0-impresso-train-de.jsonl \
  --output_path scripts/tmp/${teamname}_HIPE-2026-v1.0-impresso-train-de.jsonl
```

Then we can evaluate these predictions against the gold file:

```bash
teamname=RANDOM
python scripts/file_scorer_evaluation.py \
  --gold_data_file data/newspapers/v1.0/HIPE-2026-v1.0-impresso-train-de.jsonl \
  --predictions_file scripts/tmp/${teamname}_HIPE-2026-v1.0-impresso-train-de.jsonl
```

## Acknowledgements

The HIPE-2026 organising team expresses its sincere appreciation to the CLEF-2026 Lab Organising Committee for the overall coordination and support. HIPE-eval editions are organised within the framework of the [Impresso - Media Monitoring of the Past](https://impresso-project.ch/)￼ project, funded by the Swiss National Science Foundation under grant No. CRSII5_213585 and by the Luxembourg National Research Fund under grant No. 17498891.

## References

### HIPE-2026

**HIPE-2026 Extended overview (CEUR)**    

Juri Opitz, Maud Ehrmann, Corina Raclé, Andrianos Michail, Matteo Romanello, Emanuela Boros, Simon Gabay, and Simon Clematide. 2026. **Extended Overview of HIPE-2026: Evaluating Accurate and Efficient Person–Place Relation Extraction from Multilingual Historical Texts**. In CLEF 2026 working notes, CEUR workshop proceedings, 2026. CEUR-WS. https://doi.org/10.5281/zenodo.20344461

  
  ```bibtex
  @inproceedings{opitz_extended_2026,
    title = {Extended {{Overview}} of {{HIPE-2026}}: {{Evaluating Accurate}} and {{Efficient Person}}--{{Place Relation Extraction}} from {{Multilingual Historical Texts}}},
    booktitle = {{{CLEF}} 2026 Working Notes, {{CEUR}} Workshop Proceedings},
    author = {Opitz, Juri and Ehrmann,  Maud and Racl{\'e}, Corina and Michail, 
    Andrianos and Romanello, Matteo and Boros, Emanuela and Gabay, Simon and Clematide, Simon},
    editor = {S{\'a}nchez Salido, Eva and {Barr{\'o}n-Cede{\~n}o}, Alberto and {Garc{\'i}a Seco de Herrera}, Alba and MacAvaney, Sean and Stru{\ss}, Julia Maria},
    year = 2026,
    publisher = {CEUR-WS},
    doi = {10.5281/zenodo.20344461}
  }
  ```

**HIPE-2026 Condensed Overview (LNCS)**    

Juri Opitz, Maud Ehrmann, Corina Raclé, Andrianos Michail, Matteo Romanello and 
Simon Clematide. 2026. **Overview of HIPE-2026: Person–Place Relation Extraction from Multilingual Historical Texts**. In Experimental IR meets multilinguality, multimodality, and interaction. Proceedings of the seventeenth international conference of the CLEF association (CLEF 2026) (Lecture notes in computer science (LNCS)), 2026. Springer.

Preprint available on arXiv: [https://arxiv.org/abs/2606.25935](https://arxiv.org/abs/2606.25935)

  ```bibtex
  @inproceedings{opitz_overview_2026,
    title = {Overview of {{HIPE-2026}}: {{Person}}--{{Place Relation Extraction}} from {{Multilingual Historical Texts}}},
    booktitle = {Experimental {{IR}} Meets Multilinguality, Multimodality, and Interaction. {{Proceedings}} of the Seventeenth International Conference of the {{CLEF}} Association ({{CLEF}} 2026)},
    author = {Opitz, Juri and Ehrmann, Maud and Racl{\'e}, Corina and Michail, 
    Andrianos and Romanello, Matteo  and Clematide, Simon},
    editor = {Hagen, Matthias and Potthast, Martin and Stein, Benno and Schaer, Philipp and Zangerle, Eva and MacAvaney, Sean and Stru{\ss}, Julia Maria and S{\'a}nchez Salido, Eva and {Barr{\'o}n-Cede{\~n}o}, Alberto and {Garc{\'i}a Seco de Herrera}, Alba},
    year = 2026,
    series = {Lecture Notes in Computer Science ({{LNCS}})},
    publisher = {Springer}
  }
  ```

### Previous shared tasks

- **HIPE-2022 Participant Papers** in Working Notes of CLEF 2022 - Conference and Labs of the Evaluation Forum, edited by Faggioli, Guglielmo and Ferro, Nicola and Hanbury, Allan and Potthast, Martin.

- **HIPE-2022 Extended Overview Paper:**

  M. Ehrmann, M. Romanello, S. Najem-Meyer, A. Doucet, and S. Clematide (2022). [Extended Overview of HIPE-2022: Named Entity Recognition and Linking in Multilingual Historical Documents](http://ceur-ws.org/Vol-3180/paper-83.pdf). In Proceedings of the Working Notes of CLEF 2022 - Conference and Labs of the Evaluation Forum, edited by Guglielmo Faggioli, Nicola Ferro, Allan Hanbury, and Martin Potthast, Vol. 3180. CEUR-WS, 2022. https://doi.org/10.5281/zenodo.6979577.
    
    ```bibtex
    @inproceedings{ehrmann_extended_2022,
      title = {Extended Overview of {{HIPE-2022}}: {{Named Entity Recognition}} and {{Linking}} in {{Multilingual Historical Documents}}},
      booktitle = {Proceedings of the {{Working Notes}} of {{CLEF}} 2022 - {{Conference}} and {{Labs}} of the {{Evaluation Forum}}},
      author = {Ehrmann, Maud and Romanello, Matteo and {Najem-Meyer}, Sven and Doucet, Antoine and Clematide, Simon},
      editor = {Faggioli, Guglielmo and Ferro, Nicola and Hanbury, Allan and Potthast, Martin},
      year = {2022},
      volume = {3180},
      publisher = {{CEUR-WS}},
      doi = {10.5281/zenodo.6979577},
      url = {http://ceur-ws.org/Vol-3180/paper-83.pdf}
    }
    ```


- **HIPE-2020 Participant Papers** are in [Working Notes of CLEF 2020 - Conference and Labs of the Evaluation Forum](http://ceur-ws.org/Vol-2696/), edited by Linda Cappellato, Carsten Eickhoff, Nicola Ferro, Aurélie Névéol.

- **HIPE-2020 Extended Overview Paper**:

  M. Ehrmann, M. Romanello, A. Flückiger, and S. Clematide, [Extended Overview of CLEF HIPE 2020: Named Entity Processing on Historical Newspapers](https://infoscience.epfl.ch/record/281054) in Working Notes of CLEF 2020 - Conference and Labs of the Evaluation Forum, Thessaloniki, Greece, 2020, vol. 2696, p. 38. doi: 10.5281/zenodo.4117566.
    
  ```bibtex
  @inproceedings{ehrmann_extended_2020,
    title = {Extended {{Overview}} of {{CLEF HIPE}} 2020: {{Named Entity Processing}} on {{Historical Newspapers}}},
    booktitle = {Working {{Notes}} of {{CLEF}} 2020 - {{Conference}} and {{Labs}} of the {{Evaluation Forum}}},
    author = {Ehrmann, Maud and Romanello, Matteo and Fl{\"u}ckiger, Alex and Clematide, Simon},
    editor = {Cappellato, Linda and Eickhoff, Carsten and Ferro, Nicola and N{\'e}v{\'e}ol, Aur{\'e}lie},
    year = 2020,
    volume = {2696},
    pages = {38},
    publisher = {CEUR-WS},
    address = {Thessaloniki, Greece},
    url = {https://infoscience.epfl.ch/record/281054},
    keywords = {cited}
  }
  ```
