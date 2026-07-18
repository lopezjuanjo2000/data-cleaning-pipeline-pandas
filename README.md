# Data Cleaning & Sales Aggregation Pipeline 🐼📊

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Library-Pandas-cyan.svg?style=flat-square&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![Matplotlib](https://img.shields.io/badge/Library-Matplotlib-lightgrey.svg?style=flat-square)](https://matplotlib.org/)
[![Language](https://img.shields.io/badge/Language-Spanish%20/%20English-green.svg?style=flat-square)](#) 

**EN:** A Python-based data wrangling project implementing an end-to-end data cleaning pipeline using **Pandas**. The script processes a raw, unformatted dataset containing structural inconsistencies, missing values, and mixed date formats, converting it into a clean dataframe ready for analytical aggregation and visualization.

**ES:** Proyecto de manipulación de datos basado en Python que implementa un proceso integral de limpieza de datos utilizando **Pandas**. El script procesa un conjunto de datos sin formato que contiene inconsistencias estructurales, valores faltantes y formatos de fecha mixtos, convirtiéndolo en un dataframe limpio y listo para la agregación analítica y la visualización.

---

## 🛠️ Data Quality Issues Addressed

The raw dataset presented several common real-world data quality problems:
*   **Duplicate Entries:** Multiple identical rows for the same transaction.
*   **Missing Values (NaN/None):** Records missing critical transaction amounts or dates.
*   **Inconsistent Date Formats:** Dates stored under varying formats (`YYYY-MM-DD`, `DD/MM/YYYY`, `YYYY/MM/DD`, and `DD-MM-YYYY`).
*   **Unstructured Text:** Full addresses collapsed into a single string field.

---

## ⚙️ Pipeline Steps & Features

The script executes a sequence of data manipulation steps following a logical ETL framework:

1.  **Deduplication & Null Handling:** Removes duplicate records and filters out rows missing critical features (`Sales Amount` or `Transaction Date`).
2.  **Mixed-Format Standardization:** Leverages Pandas `to_datetime` with `format='mixed'` to robustly parse inconsistent text entries into standard `YYYY-MM-DD` timestamps.
3.  **Feature Engineering (Text Splitting):** Parses and expands the `Full Address` text column into two distinct granular dimensions: `Street` and `City`.
4.  **Temporal Aggregation:** Groups the finalized dataset by calendar months to compute cumulative monthly sales totals, mapping numeric month values into readable names using the `calendar` library.
5.  **Data Visualization:** Generates a bar chart using `matplotlib.pyplot` to visually contrast the total sales volumes across different months.

---

## 🚀 Execution & Results

### Cleaned Output Structure
After running the pipeline, data is sorted chronologically, and indexes are reset for optimal data retrieval:

| Name | Sales Amount | Transaction Date | Street | City |
| :--- | :--- | :--- | :--- | :--- |
| John Doe | 500.50 | 2024-01-15 | 123 Main St | Springfield |
| Jane Smith | 750.00 | 2024-02-15 | 456 Oak St | Springfield |
| Mike Brown | 1200.00 | 2024-03-01 | 789 Pine St | Shelbyville |
| Anna Lee | 950.75 | 2024-05-03 | 101 Maple St | Springfield |
| Mike Brown | 1200.00 | 2024-05-03 | 789 Pine St | Shelbyville |
| Lara Croft | 1450.25 | 2024-07-08 | 555 Cedar St | Capital City |
| Nina Ross | 1250.00 | 2024-07-08 | 333 Birch St | Capital City |

---

## 🛠️ How to Run

1. **Prerequisites:** Make sure you have pandas, calendar and matplotlib installed.
2. **Execution:** Clone this repository and run the Python file.

---

## 👤 Author
* **Juan José Lopez Correa** - *AI Data Analyst & Aspiring Data Scientist* - [LinkedIn](https://www.linkedin.com/in/juan-jose-lopez-correa-43898b284/)
