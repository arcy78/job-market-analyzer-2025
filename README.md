# job-market-analyzer-2025

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Status](https://img.shields.io/badge/Status-In%20Progress-yellow)
![Libraries](https://img.shields.io/badge/Libraries-Pandas%20%7C%20BeautifulSoup%20%7C%20Seaborn-green)

##  Project Overview
Ce projet a pour but d'analyser les tendances du marché de l'emploi (compétences demandées, types de postes, localisations) en utilisant une approche Data-Driven.

L'objectif est de transformer des données brutes issues d'offres d'emploi en insights stratégiques pour les candidats et recruteurs.

##  Tech Stack
* **Language:** Python
* **Scraping:** Requests, BeautifulSoup4
* **Data Manipulation:** Pandas, NumPy
* **Visualization:** Matplotlib, Seaborn
* **Environment:** Jupyter Notebook, VS Code

##  Key Insights (Preview)
Analyses préliminaires sur un dataset de test (Fake Jobs) :

![Job Market Trends](image.png)

*Le graphique ci-dessus montre la répartition des intitulés de poste les plus fréquents.*


## Project Structure
```text
├── data/               # Raw and processed datasets
├── notebooks/          # Jupyter Notebooks for exploration
├── src/                # Source code (Scrapers, Cleaning scripts)
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation
```

##  How to Run
- Clone the repository : git clone [https://github.com/arcy78/job-market-analyzer-2025.git](https://github.com/arcy78/job-market-analyzer-2025.git)
- Install dependencies : pip install -r requirements.txt
- Run the Scraper : python src/scraper.py
- Open the Notebook: Launch Jupyter Lab or VS Code to view notebooks/01_exploration.ipynb

##  Next Steps
- Connect to real Job APIs (Indeed/LinkedIn via API)
- Build an Alteryx Workflow for advanced ETL.
- Create a Power BI Dashboard for interactive visualization.
