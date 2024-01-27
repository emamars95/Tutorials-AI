# Unsupervised Learning Module 1

## Welcome
This module provides a practical guide to applying popular unsupervised learning methods for analyzing molecular dynamics data, leveraging the MD17 database from *ab initio* molecular dynamics simulations.

## Tutorial Overview

### Main Topics
- **Dimensionality Reduction**:
  - Principal Component Analysis (PCA)
  - Kernel PCA

- **Clustering Analysis**:
  - Hard partition clustering with K-Means
  - Evaluation metrics for clustering

### Requirements
To fully engage with this tutorial, the following are necessary:
- **Environment**: Jupyter Notebook (Python3, tested with version 3.8.1)
- **Python Libraries**:
  - Data processing: `pandas`, `numpy`, `scikit-learn`
  - Visualization: `seaborn`, `matplotlib`
  - Chemistry: `ase` (atomic simulation environment), `py3Dmol`
- **Online Execution**: Available via [Google Colab](https://colab.research.google.com/github)

### Learning Objectives
By the end of this tutorial, participants will be able to:
- Understand and implement dimensionality reduction techniques like PCA and Kernel PCA.
- Apply clustering analysis using K-Means and evaluate clustering results.
- Analyze molecular dynamics data to extract chemical insights.

### Dataset
- **MD17 Database**: Utilized for practical demonstrations, available at [SGDML - MD17 Database](http://www.sgdml.org/#datasets).


# Unsupervised Learning Module 2

## Overview
This tutorial is a part of the Seminars on Machine Learning in Quantum Chemistry and Quantum Computing for Quantum Chemistry (SMLQC). It focuses on applying unsupervised machine learning methods to analyze data from nonadiabatic molecular dynamics (NAMD) simulations, particularly those obtained within the surface hopping approximation. The goal is to automate pattern discovery and gain chemical insights from complex NAMD datasets.

## Tutorial Content

### Introduction to NAMD Data Analysis
- **High-Dimensional Data**: NAMD data as multivariate time series objects, representing molecular geometries and quantum properties.
- **Challenges in Manual Data Analysis**: Difficulty in identifying key internal coordinates driving excited-state dynamics.
- **Role of Unsupervised Learning**: Utilization of algorithms for clustering analysis and dimension reduction to manage high-dimensional NAMD data.

### ULaMDyn: A Python Package for NAMD Data Analysis
- **Automated Analysis Pipeline**: ULaMDyn provides a complete pipeline for analyzing NAMD trajectories data generated by the Newton-X program.
- **Pipeline Stages**:
  - Data collection from Newton-X outputs.
  - Molecular representations.
  - Dimension reduction.
  - Clustering analysis.
- **User-Friendly Interface**: Command-line interface for streamlined data analysis, alongside a detailed, step-by-step tutorial approach for flexibility and deeper understanding.

### Installation and Setup
- **Installation Instructions**: Specific guidance for setting up ULaMDyn and related packages, including necessary steps for environments like Google Colab.
- **Important Note**: Instructions to restart the execution environment post-installation to ensure proper functioning of ULaMDyn.

### Learning Objectives
- Master the application of unsupervised learning techniques in the context of NAMD.
- Develop skills in using ULaMDyn for comprehensive data analysis.
- Extract meaningful chemical insights from complex NAMD datasets.

# Molecular Dynamics with Deep Learning

## Introduction
This tutorial demonstrates how to train and deploy machine learning models for potential energy surfaces using [SchNetPack](https://github.com/atomistic-machine-learning/schnetpack), catering to both Colab and local environments.

## Tutorial Structure

### Key Steps
- **Dataset Preparation**: Guidelines for preparing datasets to train machine learning potentials with SchNetPack.
- **Model Setup**: Instructions on setting up a PaiNN model for predicting energies and forces in molecules.
- **Training and Validation**: Detailed steps for preparing the training infrastructure and the process for training and validating the model.
- **Model Deployment**: Utilizing the trained model for various predictions, including geometry optimization, frequency calculations (using [ASE](https://wiki.fysik.dtu.dk/ase/)), and molecular dynamics simulations with SchNetPack.

### Running the Local Version
1. **Environment Setup**: 
   - Creating and activating a new conda environment named `cecam_PS4`.
   - Cloning the tutorial's Git repository.
   - Executing the setup script to install required packages and datasets.
2. **Starting the Tutorial**: 
   - Launching Jupyter Notebook and selecting `CECAM_tutorial_local.ipynb`.

### Requirements
- **Google Colab Version**: Requires a Google account for execution.
- **Local Version**: Needs additional setup, including conda environment creation and package installation.

### Learning Objectives
- Gain expertise in training machine learning models for quantum molecular dynamics.
- Understand the process of deploying these models for practical applications.
- Acquire skills in using SchNetPack and PaiNN for molecular dynamics simulations and predictions.
 
---

# Computer Vision#

This folder contains a few tutorials for beginners of TensorFlow. The goal of this series of tutorial is to introduce the reader to the basic concepts of Machine Learning (ML) and, more specifically, to the Deep Learning (DL) algorithm using engaging examples and posing challenging questions.   

## Tutorial Overview

### Main Topics
- Introduction to computer vision: In this first tutorial, we move to the first steps with TensorFlow. The goal is not to explain exactly all the algorithms behind the Neural Network (NN) optimization but rather give a first feeling on the concepts behind ML. We create a simple, single-layer NN to recognize different objects from a set of images extracted from the MNIST library. 

### Requirements
To fully engage with this tutorial, the following are necessary:
- **Environment**: Jupyter Notebook (Python3)
- **Python Libraries**:
  - Data processing: `pandas`, `numpy`, `scikit-learn`, `tensorflow`
  - Visualization: `seaborn`, `matplotlib`
- **Online Execution**: Available via [Google Colab](https://colab.research.google.com/github)

