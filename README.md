# HIPE-2026-data

[HIPE 2026 shared task](https://hipe-eval.github.io/HIPE-2026/) is a [CLEF 2026 Evaluation Lab](https://clef2022.clef-initiative.eu/) on the *extraction and qualification of of person–place relations in multilingual historical documents. 
**.     

Building on the success of [HIPE-2020](https://impresso.github.io/CLEF-HIPE-2020) and [HIPE-2022](https://impresso.github.io/CLEF-HIPE-2022), which focused on entity recognition and linking, HIPE-2026 aims to support finer-grained analysis of entities and their relations, enabling digital humanities research such as reconstructing life trajectories, tracing patterns of mobility, identifying actors within local contexts, and understanding how people and places were linked in historical media ecosystems.

[Key information](#key-information)    
[Data](#data)    
[HIPE-2026 Data Releases](#hipe-2026-releases)    
[HIPE-2026 Evaluation](#hipe-2026-evaluation)    
[Acknowledgements](#acknowledgements)    
[References](#references)


## Key information
  
- :computer: Visit the [**website**](https://hipe-eval.github.io/HIPE-2026/) for general information on the shared task and registration.    

- :notebook: Read the **Participation Guidelines** (link to add  + iseally zenodo ref and badge) for detailed information about the tasks, datasets and evaluation.


- **License**: HIPE-2026 data is released under a [CC BY-NC-SA 4.0 License](https://img.shields.io/badge/License-CC_BY--NC--SA_4.0-lightgrey.svg) [![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC_BY--NC--SA_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-sa/4.0/)

- **Where to find the data**:      
      - in the [data](https://github.com/hipe-eval/HIPE-2026-data/tree/main/data/) folder     
      - in git [releases](https://github.com/hipe-eval/HIPE-2026-data/releases)      
      - on [zenodo](to be updated)
      
- **Release history**:    
      - 10.12.2025: partial training data release [v1.0](link to git release)    
      - 19.01.2026: full training and dev data release [v2.0](link to git releas)    
      - xx.xx.2026: masked test data release [v2.1](https://github.com/hipe-eval/HIPE-2022-data/releases/tag/v2.1)   
      - xx.xx.2022: unmasked test data release

## Data

HIPE-2026 builds on the [HIPE-2022 v2.1](https://github.com/hipe-eval/HIPE-2022-data/tree/main/data/v2.1) NE-annotated historical newspaper datasets. We focus on the datasets that include PERS and LOC annotations (`impresso-hipe-2020`, `newseye`, `sonar`, and `letemps`).

[A bit more info on data preparation]



## HIPE-2026 releases 

### Format and structure
See https://github.com/hipe-eval/HIPE-2022-data/tree/main for writing info here. Will be much shorter.


### Directory structure, naming conventions and versioning:

HIPE-2026 data directory is organised per HIPE release version, dataset and language, as follows:

Tree below: to be udpated
```
data
└── vx.x
  └── dataset1
  │   ├── lg1
  │   │   ├── HIPE-2022-vx.x-dataset1-train-lg1.tsv
  │   │   ├── HIPE-2022-vx.x-dataset1-dev-lg1.tsv
  │   └── lg2
  │       ├── HIPE-2022-vx.x-dataset2-train-lg2.tsv
  │       ├── HIPE-2022-vx.x-dataset2-dev-lg2.tsv
  └── dataset2
  │   ├── lg1
  │   │   ├── HIPE-2022-vx.x-dataset2-train-lg1.tsv
  │   │   ├── ...
  └── ...
```

**Files and file naming conventions**

- Training and development datasets consist of UTF-8 JSON Line files
- There is one `.jsonl` file per dataset, language and dataset split.
- Files are named according to this schema:
  `HIPE-2022-<hipeversion>-<dataset-alias>-<split>-<language>.tsv` where `# split = sample|train|dev|dev2|test|`. For example, the file `HIPE-2022-v1.0-newseye-dev-sv.tsv` contains NE-annotated documents of the Swedish part of the newseye corpus which are meant as development set, in HIPE format and from HIPE-2022 release v1.0. 
     

**Versioning**  

- HIPE-2026 release are versioned with a two-part version number (Major.Minor) which is present in 1) the data directory structure and 2) the filename of each file.     
- Each HIPE-2026 release has an equivalent git repository release, with release notes.    
- The version of a primary dataset is mentioned in its document metadata (see below).    


### Dataset statistics

Link to notebook when available.

## HIPE-2022 Evaluation



## Acknowledgements

The HIPE 2026 organizing team expresses her greatest appreciation to the CLEF-2026 Lab Organising Committee for the overall organization, to....to be updated.

## References

### About HIPE-2026

- link to ECIR paper




### Previous shared task 

 Potthast, Martin.

- **CEUR HIPE-2020 Extended Overview Paper (open access):**

M. Ehrmann, M. Romanello, S. Najem-Meyer, A. Doucet, and S. Clematide (2022). [Extended Overview of HIPE-2022: Named Entity Recognition and Linking in Multilingual Historical Documents](http://ceur-ws.org/Vol-3180/paper-83.pdf). In Proceedings of the Working Notes of CLEF 2022 - Conference and Labs of the Evaluation Forum, edited by Guglielmo Faggioli, Nicola Ferro, Allan Hanbury, and Martin Potthast, Vol. 3180. CEUR-WS, 2022. https://doi.org/10.5281/zenodo.6979577.


```
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

- **LNCS HIPE-2020 Condensed Lab Overview Paper:**

M. Ehrmann, M. Romanello, S. Najem-Meyer, A. Doucet, and S. Clematide (2022). [Overview of HIPE-2022: Named Entity Recognition and Linking in Multilingual Historical Documents](). In: Experimental IR Meets Multilinguality, Multimodality, and Interaction. Proceedings of the Thirteenth International Conference of the CLEF Association (CLEF 2022). Lecture Notes in Computer Science. Springer, Cham (link to [accepted version](https://github.com/hipe-eval/HIPE-2022/blob/main/assets/pdf/HIPE_2022_LNCS_CondensedLabOverview_accepted_version.pdf)).

```
@inproceedings{hipe2022_condensed_2022,
  title     = {{Overview of HIPE-2022: Named Entity Recognition and Linking in Multilingual Historical Documents}},
  booktitle = {{Experimental IR Meets Multilinguality, Multimodality, and Interaction. Proceedings of the Thirteenth International Conference of the CLEF Association (CLEF 2022)}},
  series    = {Lecture Notes in Computer Science (LNCS)},
  publisher = {Springer},
  author    = {Ehrmann, Maud and Romanello, Matteo and Najem-Meyer, Sven and Doucet, Antoine and Clematide, Simon},
  year      = {2022},
  editor    = {Barrón-Cedeño, Alberto and Da San Martino, Giovanni and Degli Esposti, Mirko and Sebastiani, Fabrizio and Macdonald, Craig and Pasi, Gabriella and Hanbury, Allan and Potthast, Martin and Faggioli, Guglielmo and Ferro, Nicola
}
```

- **ECIR-2022 Introduction Short Paper:**    

M. Ehrmann, M. Romanello, A. Doucet, and S. Clematide (2022). [Introducing the HIPE 2022 Shared Task: Named Entity Recognition and Linking in Multilingual Historical Documents](https://doi.org/10.1007/978-3-030-99739-7_44). In: Advances in Information Retrieval. ECIR 2022. Lecture Notes in Computer Science, vol 13186. Springer, Cham (link to [postprint](https://github.com/hipe-eval/HIPE-2022/blob/main/assets/pdf/HIPE2022_ECIR_shortpaper_postprint.pdf)).

```
@inproceedings{ehrmann_introducing_2022,
  title     = {{Introducing the HIPE 2022 Shared Task:Named Entity Recognition and Linking in Multilingual Historical Documents}},
  booktitle = {Proceedings of the 44\textsuperscript{d} European Conference on {{IR}} Research ({{ECIR}} 2022)},
  author    = {Ehrmann, Maud and Romanello, Matteo and Clematide, Simon and Doucet, Antoine},
  year      = {2022},
  publisher = {{Lecture Notes in Computer Science, Springer}},
  address   = {{Stavanger, Norway}},
  url       = {https://link.springer.com/chapter/10.1007/978-3-030-99739-7_44}
}
```

- M. Ehrmann, M. Romanello, A. Flückiger, and S. Clematide, [Extended Overview of CLEF HIPE 2020: Named Entity Processing on Historical Newspapers](https://infoscience.epfl.ch/record/281054) in Working Notes of CLEF 2020 - Conference and Labs of the Evaluation Forum, Thessaloniki, Greece, 2020, vol. 2696, p. 38. doi: 10.5281/zenodo.4117566. 

- CLEF-HIPE-2020 Participant Papers in [Working Notes of CLEF 2020 - Conference and Labs of the Evaluation Forum](http://ceur-ws.org/Vol-2696/), edited by Linda Cappellato, Carsten Eickhoff, Nicola Ferro, Aurélie Névéol.

- CLEF-HIPE-2020 Workshop [Presentation Video Recordings](https://www.youtube.com/playlist?list=PLB45F159nVx-3bee7G_1jdTfUAtsLD0FU).









