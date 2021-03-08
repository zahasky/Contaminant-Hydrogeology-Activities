# Contaminant Hydrogeology Activities
Welcome to the Contaminant Hydrogeology Modeling Activities wiki page. This page provides an overview and table of contents for the different activities covered in each module of the class. These activities have been written and organized to make them a resource for people interested in learning more about quantitatively describing contaminant transport even if you are not taking the GEOSCI/GEOENG 629 at the University of Wisconsin-Madison.

# Table of Contents
### Introduction
Before you can run these activities you will need to have Python and MODFLOW set up on your workstation. These first two notebooks provide instructions for setup and introduce some of the common operations and functions that we will utilize in Python.
   * [Getting started](https://github.com/zahasky/Contaminant-Hydrogeology-Modeling-Activities/blob/master/MODFLOW%2C%20Python%2C%20and%20FloPy%20Setup.ipynb)- This notebook provides links to install Python, MODFLOW, and set up FloPy.
   * [Introduction to Python](https://github.com/zahasky/Contaminant-Hydrogeology-Modeling-Activities/blob/master/Python%20Introduction%20for%20629.ipynb)- This notebook will introduce Python syntax and basic operations required to solve problems, build models, and plot results.
### Conservative solute transport module
This first module is where we introduce the fundamental concepts of solute transport in porous media--advection, dispersion, and diffusion. These mechanisms are described mathematically with the advection-dispersion equation. The activities in the module consist of both analytical and numerical modeling approaches for solving the ADE and introduce methods for parameterizing these transport mechanisms.
1. Conservative solute transport analytical solutions
   * [Diffusion](https://github.com/zahasky/Contaminant-Hydrogeology-Modeling-Activities/blob/master/Diffusion%20Analytical%20Demo.ipynb)
   * [Dispersion and superposition of analytical solutions](https://github.com/zahasky/Contaminant-Hydrogeology-Modeling-Activities/blob/master/Dispersion%20Analytical%20Demo.ipynb)
   * [Introduction to moment analysis](https://github.com/zahasky/Contaminant-Hydrogeology-Activities/blob/master/Intro%20to%20Moment%20Analysis.ipynb)
2. Conservative solute transport FloPy modeling
   * [Building the first model in FloPy](https://github.com/zahasky/Contaminant-Hydrogeology-Activities/blob/master/FloPy%20Introduction.ipynb)
   * [Building a FloPy model into a Python function](https://github.com/zahasky/Contaminant-Hydrogeology-Modeling-Activities/blob/master/FloPy%201D%20Function.ipynb)
   * [Two-dimensional model to illustrate macrodispersion](https://github.com/zahasky/Contaminant-Hydrogeology-Activities/blob/master/FloPy%202D%20Macrodispersion%20Illustration.ipynb)

### Reactive transport module
1. [Sorption isotherm functions and plots](https://github.com/zahasky/Contaminant-Hydrogeology-Activities/blob/master/Sorption%20Isotherms.ipynb)
2. [Reactive transport analytical solutions](https://github.com/zahasky/Contaminant-Hydrogeology-Activities/blob/master/First%20Order%20Reactions.ipynb)
3. [Reactive transport FloPy model](https://github.com/zahasky/Contaminant-Hydrogeology-Activities/blob/master/FloPy%201D%20Reactions.ipynb)

### Multiphase contaminant hydrogeology module
1. [Capillary pressure functions](https://github.com/zahasky/Contaminant-Hydrogeology-Activities/blob/master/Capillary%20Pressure%20Curves.ipynb)
2. [Relative permeability functions and relationships to capillary pressure](https://github.com/zahasky/Contaminant-Hydrogeology-Activities/blob/master/Relative%20Permeability%20Curves.ipynb)

### Colloid contaminant hydrogeology module
1. [Colloid filtration theory and first order deposition coefficients](https://github.com/zahasky/Contaminant-Hydrogeology-Activities/blob/master/Colloid%20Filtration%20Theory%20and%20Deposition%20Rate%20Coefficients.ipynb)
2. [Impact of heterogeneous microzones on bulk transport behavior](https://github.com/zahasky/Contaminant-Hydrogeology-Activities/blob/master/FloPy%20Anaerobic%20Microzones.ipynb)

### Contaminant remediation module
1. Limits of pumping in heterogeneous aquifers
2. PFAS immobilization with sorptive barrier
