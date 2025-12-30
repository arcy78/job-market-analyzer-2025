import requests
from bs4 import BeautifulSoup
import pandas as pd
import os
from datetime import datetime

# --- CONFIGURATION ---
URL = "https://realpython.github.io/fake-jobs/"
OUTPUT_PATH = "data/raw/jobs_data.csv"

def scrape_jobs():
    """
    Fonction principale pour récupérer les données,
    les nettoyer sommairement et les sauvegarder.
    """
    print(f"🚀 Démarrage du scraping sur : {URL}")
    
    # 1. REQUÊTE HTTP (Récupération du code HTML)
    try:
        response = requests.get(URL)
        response.raise_for_status() # Vérifie si la requête a réussi (Code 200)
    except requests.exceptions.RequestException as e:
        print(f"❌ Erreur lors de la requête : {e}")
        return

    # 2. PARSING (Analyse du HTML)
    soup = BeautifulSoup(response.content, "html.parser")
    results = soup.find(id="ResultsContainer")
    job_elements = results.find_all("div", class_="card-content")

    print(f"ℹ️  {len(job_elements)} offres trouvées. Extraction en cours...")

    # Liste pour stocker les données
    jobs_list = []

    # 3. EXTRACTION DES DONNÉES (Boucle sur chaque offre)
    for job in job_elements:
        title = job.find("h2", class_="title").text.strip()
        company = job.find("h3", class_="company").text.strip()
        location = job.find("p", class_="location").text.strip()
        date_posted = job.find("time").text.strip() if job.find("time") else datetime.now().strftime("%Y-%m-%d")

        # Ajout dans notre liste
        jobs_list.append({
            "title": title,
            "company": company,
            "location": location,
            "date_collected": date_posted
        })

    # 4. SAUVEGARDE (Dataframe -> CSV)
    # On crée le dossier s'il n'existe pas
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    
    df = pd.DataFrame(jobs_list)
    df.to_csv(OUTPUT_PATH, index=False)
    
    print(f"✅ Succès ! Les données ont été sauvegardées dans : {OUTPUT_PATH}")
    print(f"📊 Aperçu des 5 premières lignes :\n")
    print(df.head())

if __name__ == "__main__":
    scrape_jobs()