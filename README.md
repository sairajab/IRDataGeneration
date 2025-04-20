# IRDataGeneration

This repository provides a pipeline to use **SpliceGrapher** and **iDiffIR** to generate Intron Retention (IR) data.

## Setup Instructions

### 1. Install SpliceGrapher (version 2.7.0)

- Download from the official website:  
  [https://splicegrapher.sourceforge.net/index.html](https://splicegrapher.sourceforge.net/index.html)

### 2. Prepare Genome Annotation

- Obtain the genome annotation file in GTF format (e.g., `your_annotation_file.gtf`).

### 3. Generate Splice Graphs

Run the following command to generate splice graphs for each gene:

```bash
gene_model_to_splicegraph.py -m your_annotation_file.gtf -a -S -d reference
```
This will create a folder named reference containing splice graphs for each gene.

### 4. Extract Alternative Splicing Events

```bash
python get_AS_From_splicegrpah.py IR path/to/reference
```
This command generates a ```.txt``` file listing all IR events. 

### 5. Get All Introns in the Genome

Get All Introns for the Genome
Use this repository to generate a list of all introns: https://github.com/sairajab/RetrieveIntrons

### 6. Get Retained Introns

```bash
python get_retained_introns_from_IRevents.py
```
This will create a ```.txt``` file containing retained introns. Modify the following parameters. 

```ir_events_file```: path to the IR events .txt file

```introns_file```: path to the all-introns file

```output_file```: name for the output file containing retained introns



