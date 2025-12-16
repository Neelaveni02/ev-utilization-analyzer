# Electric Vehicle (EV) Charging Station Utilization Analyzer

## Student Information
**Name:** Neelaveni Ushakela  
**Email:** nushakel@stevens.edu  

---

## Project Description
With the rapid adoption of Electric Vehicles (EVs), effective utilization of public charging stations has become a critical challenge. Many charging stations experience uneven usage—some are heavily congested while others remain underutilized. This imbalance leads to user inconvenience and inefficient infrastructure planning.

This project, **Electric Vehicle (EV) Charging Station Utilization Analyzer**, analyzes real-world EV charging session data to compute charging station utilization, identify overused and underused stations, and provide actionable recommendations for optimization. The project uses real data from the Caltech Adaptive Charging Network (ACN) and demonstrates object-oriented programming, data analysis, testing, and advanced Python features.

---

## Dataset
**Source:** Caltech Adaptive Charging Network (ACN-Data)  
**Website:** https://ev.caltech.edu/dataset  

**Dataset Details:**
- Site: Caltech
- Time Range: January 1, 2019 – December 31, 2019
- Number of Sessions: 10,607
- Original Format: JSON
- Processed Format: CSV

Each record represents a single charging session and includes fields such as:
- `connectionTime`
- `disconnectTime`
- `doneChargingTime`
- `kWhDelivered`
- `stationID`
- `siteID`

The JSON dataset was converted to CSV for easier processing using the pandas library.

---

## Program Structure
ev-utilization-analyzer/
├── data/
│ ├── raw/ # Original dataset (JSON, CSV)
│ └── processed/ # Processed outputs
├── notebooks/
│ └── EV_Utilization_Analyzer.ipynb
├── src/
│ ├── station.py # Station class and utilization logic
│ ├── network.py # ChargingNetwork class (composition)
│ ├── analysis.py # Utilization analysis functions
│ ├── io_utils.py # Data loading utilities
│ ├── exceptions.py # Custom exception classes
│ └── sessions.py # Generator for charging sessions
├── tests/
│ ├── test_utilization.py # Utilization test cases
│ └── test_data_format.py # Data integrity tests
├── conftest.py
├── requirements.txt
└── README.md


---

## How to Run the Program

### 1. Install Dependencies
```bash
pip install -r requirements.txt

2. Run the Jupyter Notebook

Open the notebook:

notebooks/EV_Utilization_Analyzer.ipynb


The notebook:

Loads the dataset

Builds Station and ChargingNetwork objects

Computes utilization metrics

Displays results

Provides a menu-driven interface

3. Run Tests
pytest


All tests pass successfully.