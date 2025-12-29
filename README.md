
# IE221 Team Work – Group 12

## Project Description
This project experimentally verifies the Strong Law of Large Numbers (SLLN) 
and the Central Limit Theorem (CLT). In addition, a practical application of 
the SLLN is demonstrated using Monte Carlo estimation of the number π.

## Team Members
-Fatma Melek Genç – 2311021015
- Nisanur Turgut– 2213011003
- Elif Gültekin  – 2211021047
- Pınar Zehra Bulut – 2311021060

## Installation
Install the required Python libraries using the following command:

```bash
python -m pip install numpy matplotlib scipy



#usage
python src/slln_simulation.py
python src/clt_simulation.py
python src/monte_carlo_pi.py

#Project Structure
IE221-TeamWork-Group12/
├── src/
│   ├── slln_simulation.py
│   ├── clt_simulation.py
│   └── monte_carlo_pi.py
├── results/
│   └── figures/
│       ├── slln_convergence.png
│       ├── clt_histograms.png
│       ├── clt_qqplots.png
│       └── pi_estimation.png
├── reports/
├── README.md
└── requirements.txt

