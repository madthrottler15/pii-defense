Real Time PII Detector
Detects and redacts PII (phone, aadhar, passport, UPI, combinatorial fields).
Adds is_pii column for classification.
Ensures no standalone false positives like single email, single name, city, etc.

Files
detector_Hardikkumar_Patel.py → Main script
redacted_output_Hardikkumar_Patel.csv → Output file
iscp_pii_dataset.csv → Input dataset

Usage
python3 detector_Hardikkumar_Patel.py iscp_pii_dataset.csv
