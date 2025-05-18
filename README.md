# Submission Pemda: ETL Pipeline Project

## **Project Description**

This project is an implementation of an **ETL (Extract, Transform, Load) Pipeline** for web scraping product data from the [Fashion Studio Dicoding](https://fashion-studio.dicoding.dev/) website. The extracted data includes:

* **Title** → Product name
* **Price** → Product price
* **Rating** → Product rating
* **Colors** → Available colors
* **Size** → Product sizes
* **Gender** → Gender category

After extraction, the data undergoes a transformation process before finally being stored in **CSV** or **Google Sheets** format.

---

## **Project Structure**

```plaintext
ETL-Pipeline-Project-main
├── tests
│   ├── test_extract.py
│   ├── test_transform.py
│   └── test_load.py
│
├── utils
│   ├── extract.py        # Data extraction from the website
│   ├── transform.py      # Data transformation process
│   └── load.py           # Data storage to the repository
│
├── main.py               # Main ETL program
├── requirements.txt      # Required dependencies
├── submission.txt        # Technical explanation and results
├── products.csv          # Scraped data in CSV format
├── google-sheets-api.json # API credentials for Google Sheets
```

---

## **How to Run the Project**

1️⃣ **Clone the repository**

```bash
git clone https://github.com/insanniaa/ETL-Pipeline-Project.git
cd ETL-Pipeline-Project-main
```

2️⃣ **Install dependencies**

```bash
pip install -r requirements.txt
```

3️⃣ **Run the ETL Pipeline**

```bash
python3 main.py
```

4️⃣ **Run Unit Tests** 

```bash
coverage run -m pytest tests
```
