# Real Time PII Detector
Detect and redact Personally Identifiable Information (PII) in JSON data stored inside CSV files. This tool focuses on key PII types like phone numbers, Aadhaar numbers, passports, UPI IDs, and combinations of fields to avoid false positives.

## Feature
- Detects and redacts PII (phone, aadhar, passport, UPI, combinatorial fields)
  
## Files
- `detector_Samarth_K.py` → Main script
- `redacted_output_Samarth_K.csv` → Output file
- `iscp_pii_dataset.csv` → Input dataset

## Usage
```bash
python3 detector_Samarth_K.py iscp_pii_dataset.csv
```


