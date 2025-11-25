# HIPE-2026-data

[HIPE 2026 shared task](https://hipe-eval.github.io/HIPE-2026/) is a [CLEF 2026 Evaluation Lab](https://clef2022.clef-initiative.eu/) on the **extraction and qualification of of person–place relations in multilingual historical documents.**.     

Building on the success of [HIPE-2020](https://impresso.github.io/CLEF-HIPE-2020) and [HIPE-2022](https://impresso.github.io/CLEF-HIPE-2022), which focused on entity recognition and linking, HIPE-2026 aims to support answering the question **_Who was where, when?_** and to deepen our understanding of how people and places were connected in historical media. This will enable the reconstruction of life trajectories, the tracing of mobility patterns, and the identification of actors within local contexts.

[Key information](#key-information)    
[Data](#hipe-2026-data)    
[HIPE-2026 Data Releases](#hipe-2026-releases)    
[HIPE-2026 Evaluation](#hipe-2026-evaluation)    
[Acknowledgements](#acknowledgements)    
[References](#references)

## Key information
  
- :computer: Visit the [**website**](https://hipe-eval.github.io/HIPE-2026/) for general information on the shared task and registration.    
- :notebook: Read the [**Participation Guidelines**](to-be-updated) for detailed information about the tasks, datasets and evaluation.
- **License**: HIPE-2026 data is released under a [CC BY-NC-SA 4.0 License](https://img.shields.io/badge/License-CC_BY--NC--SA_4.0-lightgrey.svg) [![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC_BY--NC--SA_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-sa/4.0/)
- **Where to find the data**:      
      - in the [data](https://github.com/hipe-eval/HIPE-2026-data/tree/main/data/) folder     
      - in git [releases](https://github.com/hipe-eval/HIPE-2026-data/releases)      
      - later: also on zenodo.
- **Release history**:    
      - 01.12.2026: data sample (example) 
      - 10.12.2025: partial training data release [v1.0](link to git release)    
      - 19.01.2026: full training and dev data release [v2.0](link to git releas)    
      - xx.xx.2026: masked test data release    
      - xx.xx.2022: unmasked test data release

## HIPE-2026 data

**Contents and preparation**

HIPE-2026 builds on the [HIPE-2022 v2.1](https://github.com/hipe-eval/HIPE-2022-data/tree/main/data/v2.1) NE-annotated historical newspaper datasets. 

Primary datasets included in the HIPE-2026 data are those that include PERS and LOC annotations, namely:`impresso-hipe-2020`, `newseye`, `sonar`, and `letemps`.

HIPE-2022 data in IOB format, containing NE mentions and Wikidata QIDs, is converted into JSON, preserving the document text and metadata, and enabling the extraction of person–place pairs. 

The preparation process involved roughly the following steps:    
   1. Representation transformation: convert IOB-encoded annotations into structured JSON (intermediate JSON schema). 
   2. Data cleaning & filtering: merge NIL entities and remove overly long documents. 
   3. Extraction of candidate person–location pairs: identify potential pairs within each document and filter. 
   4. Annotation — pre-annotate with an LLM, then manually review and correct collaboratively. 
   5. Final dataset creation: assemble dataset splits and package for release (final JSON schema). 

**Format and data representation**

- HIPE-2026 data follows this [JSON schema]().
- All documents from different primary datasets of HIPE-2022 are gathered in the same language-dependent JSON Line file.
- Information on the source document and its metadata are in the `media` property.

**Directory structure and naming convention**

- Training and development datasets consist of UTF-8 JSON Line files. There is one `.jsonl` file per language and split.
- Files are named according to this schema: `HIPE-2026-vx.x-impresso-<train|dev|test>-<lg1>.jsonl`.
- Data directory is organised per HIPE release version and language:

    ```
    data
    └── vx.x
         ├── lg1
         │     ├── HIPE-2022-vx.x-dataset1-train-lg1.jsonl
         │     ├── HIPE-2022-vx.x-dataset1-dev-lg1.jsonl
         └── lg2
         │     ├── HIPE-2022-vx.x-dataset2-train-lg2.jsonl
         │     ├── HIPE-2022-vx.x-dataset2-dev-lg2.jsonl
         ├── ...
    └── vx.x
        ├── lg1 ...
    ```

**Versioning**  

- HIPE-2026 releases are versioned `Major.Minor`. Version informatio is present in the data directory structure and data filenames.     
- Each HIPE-2026 release has an equivalent git repository release, with release notes.    
   

### Dataset statistics

_To come soon: Link to notebook when available._


## Acknowledgements

The HIPE-2026 organising team expresses its sincere appreciation to the CLEF-2026 Lab Organising Committee for the overall coordination and support. HIPE-eval editions are organised within the framework of the [Impresso - Media Monitoring of the Past](https://impresso-project.ch/)￼ project, funded by the Swiss National Science Foundation under grant No. CRSII5_213585 and by the Luxembourg National Research Fund under grant No. 17498891.


## References

### HIPE-2026

_To be updated_


### Previous shared tasks

- **HIPE-2022 Participant Papers** in Working Notes of CLEF 2022 - Conference and Labs of the Evaluation Forum, edited by Faggioli, Guglielmo and Ferro, Nicola and Hanbury, Allan and Potthast, Martin.   

- **HIPE-2022 Extended Overview Paper:**

    M. Ehrmann, M. Romanello, S. Najem-Meyer, A. Doucet, and S. Clematide (2022). [Extended Overview of HIPE-2022: Named Entity Recognition and Linking in Multilingual Historical Documents](http://ceur-ws.org/Vol-3180/paper-83.pdf). In Proceedings of the Working Notes of CLEF 2022 - Conference and Labs of the Evaluation Forum, edited by Guglielmo Faggioli, Nicola Ferro, Allan Hanbury, and Martin Potthast, Vol. 3180. CEUR-WS, 2022. https://doi.org/10.5281/zenodo.6979577.
    
    <details>
    <summary>bibtex</summary>
    
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
    
    <pre>
    </pre>
    </details>

- **HIPE-2020 Participant Papers** are in [Working Notes of CLEF 2020 - Conference and Labs of the Evaluation Forum](http://ceur-ws.org/Vol-2696/), edited by Linda Cappellato, Carsten Eickhoff, Nicola Ferro, Aurélie Névéol.

- **HIPE-2020 Extended Overview Paper**:

   M. Ehrmann, M. Romanello, A. Flückiger, and S. Clematide, [Extended Overview of CLEF HIPE 2020: Named Entity Processing on Historical Newspapers](https://infoscience.epfl.ch/record/281054) in Working Notes of CLEF 2020 - Conference and Labs of the Evaluation Forum, Thessaloniki, Greece, 2020, vol. 2696, p. 38. doi: 10.5281/zenodo.4117566.

  <details>
  <summary>bibtex</summary>
    
  ```bibtex
  @inproceedings{ehrmann_extended_2020,
    ids = {ehrmann2020extended,ehrmann_extended_2020a},
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

  <pre>
  </pre>
  </details>












