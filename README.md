# Promoter Calculator
## Introduction
A pip installable Python package for predicting transcription initiation rates for any σ70 promoter sequence.  
The Promoter Calculator was orginally built by Travis La Fleur, Ayaan Hossain, and Howard Salis.
```
# Promoter Calculator
Python implementation of the Promoter Calculator v1.0 by Travis La Fleur, Ayaan Hossain, and Howard Salis

When using this code, remember to cite its publication: La Fleur, Travis L., Ayaan Hossain, and Howard M. Salis. "Automated Model-Predictive Design of Synthetic Promoters to Control Transcriptional Profiles in Bacteria." bioRxiv (2021)

Correspondence should be addressed to H.M.S. (salis@psu.edu).

Abstract:
Transcription rates are regulated by the interactions between RNA polymerase, sigma factor, and promoter DNA sequences in bacteria. However, it remains unclear how non-canonical sequence motifs collectively control transcription rates. Here, we combined massively parallel assays, biophysics, and machine learning to develop a 346-parameter model that predicts site-specific transcription initiation rates for any σ70 promoter sequence, validated across 17396 bacterial promoters with diverse sequences. We applied the model to predict genetic context effects, design σ70 promoters with desired transcription rates, and identify undesired promoters inside engineered genetic systems. The model provides a biophysical basis for understanding gene regulation in natural genetic systems and precise transcriptional control for engineering synthetic genetic systems.
```
## Installation
To install the Promoter Calculator, run the following command:
```
pip install git+https://github.com/JinyuanSun/PromoterCalculator.git@lite
```
To test the installation, run the following command:
```
cd test
python run.py
```
## Usage
To use the Promoter Calculator in a python scripy:
```python
from promoter_calculator import Promoter_Calculator

input_seq = "GACAAGTTGTCAGTTATCTCTTCGGATATTTGTCTATTTCGTCCGAAATATTGTCAGTCGAACTCGGGTGAATACGTTTGGC"

calc = Promoter_Calculator()
calc.run(input_seq, TSS_range=[60, len(input_seq)])
output = calc.output()
print(output)
```