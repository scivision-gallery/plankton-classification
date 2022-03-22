<div align="center">
    <h1>Plankton Images Classification</h1>
</div>

<p align="center">
    <a href="https://github.com/scivision-gallery/plankton-classification/blob/main/LICENSE">
        <img alt="License" src="https://img.shields.io/badge/License-MIT-yellow.svg">
    </a>
    <a href="https://mybinder.org/v2/gh/scivision-gallery/plankton-classification.git/main?labpath=plankton_classification_cefas.ipynb">
        <img alt="Binder" src="https://mybinder.org/badge_logo.svg">
    </a>
    <a href="https://github.com/scivision-gallery/plankton-classification/workflows/ci/badge.svg">
        <img alt="Continuous integration badge" src="https://github.com/scivision-gallery/plankton-classification/workflows/ci/badge.svg">
    <br/>
</p>

<p align="center">
  <img src="https://github.com/scivision-gallery/plankton-classification/blob/main/figs/plankton_prediction_example.png?raw=true" 
        alt="Images classification in three classes: copepod, non-copepod and detritus" width="60%" align="center">
</p>

<p align="center">
    <em>
    Classification of sample images collected by CEFAS Plankton Imager. Three classes: copepod, non-copepod and detritus. 
    </em>
</p>

## Abstract
Plankton plays an essential role in the global carbon cycle and carbon sequestration, regulating the exchange of carbon dioxide between the atmosphere, surface ocean and ultimately the seabed. Plankton is also used in global monitoring efforts providing reliable and sensitive indicators to climate change and ecosystem health.

As part of a Data Study Group (DSG) challenge organised between the Alan Turing Institute, the Centre for Environment, Fisheries and Aquaculture Science (CEFAS) and Plankton Analytics Ltd (see [here](https://www.turing.ac.uk/events/data-study-group-november-2021)), the participants contributed in the use of pretrained Convolutional Neural Networks (CNNs) with a ResNet-50 architecture to improve the accuracy of plankton classification at finer taxonomic levels compared to a baseline Random Forest.

In this notebook, we demonstrate how `scivision` facilitates the discovery of one of the trained ResNet-50 CEFAS DSG models for classifying plankton images into three classes: copepod, non-copepod and detritus. We pair the model with one of the matched data sources from the scivision data catalog, in this case a relatively small sample of images (n=26) extracted from the full test set (N=5863) used during the DSG challenge.

## How to run

The notebook is designed to be launched from Binder.
* Click the **Launch Binder** button at the top level of the repository

You may also download the notebook from GitHub to run it locally:
* Open your terminal
* Check your conda install with `conda --version`. If you don't have conda, install it by following these instructions (see [here](https://docs.conda.io/en/latest/miniconda.html))
* Clone the repository, `https://github.com/scivision-gallery/plankton-classification.git` 
* Move into the cloned repository, `cd plankton-classification`
* Install the dependencies, `conda env create -f environment.yml`
* Activate the installed environment, `conda activate plankton-classification-scivision`
* Launch the jupyter interface of your preference, notebook, `jupyter notebook` or lab `jupyter lab`

## Acknowledgment 
This notebook was supported by the outcomes of the [CEFAS DSG challenge in November 2021](https://www.turing.ac.uk/events/data-study-group-november-2021). The scivision team thanks the individuals and institutions involved in the Plankton DSG, in particular CEFAS for providing one of the trained models and sample images used in this notebook.
