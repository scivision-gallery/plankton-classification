# Classification of plankton images using ResNet-50 CEFAS DSG model

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/scivision-gallery/plankton-classification.git/HEAD?labpath=plankton_classification_cefas.ipynb)

Notebook demonstrating a ResNet-50 model trained during CEFAS DSG challenge classifying sample plankton images gathered by the Plankton Imager system into three classes: copepod, non-copepod and detritus.

## How to run

The notebook is designed to be launched from Binder.
* Click the **Launch Binder** button at the top level of the repository

You may also download the notebook from GitHub to run it locally:
* Open your terminal
* Check your conda install with conda --version. If you don't have conda, install it by following the official Conda instructions (see [here](https://docs.conda.io/en/latest/miniconda.html))
* Clone the repository, `https://github.com/scivision-gallery/plankton-classification.git` 
* Move into the cloned repository, `cd plankton-classification`
* Install the dependencies, `conda env create -f environment.yml`
* Activate the installed environment, `conda activate plankton-classification-scivision`
* Launch the jupyter interface of your preference, notebook, `jupyter notebook` or lab `jupyter lab`

## Acknowledgment 
This notebook was supported by the outcomes of the [CEFAS DSG challenge in November 2021](https://www.turing.ac.uk/events/data-study-group-november-2021). The scivision team thanks the participants and challenge owner of the Plankton DSG, in particular the Centre for Environment, Fisheries and Aquaculture Science (CEFAS) for providing one of the trained models and sample images used in this notebook.