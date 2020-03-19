# example-compendium

This example compendium illustrates a simple organizational structure for a project. 

## Prerequisites

To run this compendium, you'll need to have conda installed. I recommend [miniconda](https://docs.conda.io/en/latest/miniconda.html), but [Anaconda](https://docs.anaconda.com/anaconda/install/) would also work.

## Quickstart

### Create and activate the conda environment

From the terminal, create the conda environment for this project:

```bash
conda env create -f environment.yml
```

Then activate the environment:

```bash
conda activate denvertraffic
```


### Execute the compendium

To run the analysis run GNU Make from the terminal:

```bash
make
```

## Details

Here's what's inside: 

### `analysis/`

All scripts that are necessary to run the analysis (in this case, `.py` files).

### `data/`

A place for `raw/` and `clean/` data. 
Notice here, that there are `.gitignore` files in the subdirectories that
tell Git not to track CSV files. 
This is useful as a way to maintain the directory structure, while ignoring 
certain files in subdirectories (as opposed to adding a line for `data/raw/`
in the top-level `.gitignore` file).

### `figures/` 

A location for generated figures. 
This also has a `.gitignore` file so that the directory exists in the 
repository, but generated figures in the `figures/` directory are not tracked. 

### `paper/`

The place to store files related to the paper or report. 
Note that we are not tracking the generated `report.pdf` file. 

### `Makefile` 

This file contains instructions for how to execute the compendium. 

