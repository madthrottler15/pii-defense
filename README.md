**Real Time PII Detector**

Detect and redact Personally Identifiable Information (PII) in JSON data stored inside CSV files. This tool focuses on key PII types like phone numbers, Aadhaar numbers, passports, UPI IDs, and combinations of fields to avoid false positives.

**Features**

Detects & redacts standalone PII:

Phone (10 digits)

Aadhaar (12 digits)

Passport (India-specific format)

UPI ID

Combinatorial PII detection: Requires 2 or more among name, email, address, IP address to trigger redaction.

Minimizes false positives: Single email, single name, or city alone are not flagged as PII.

Outputs CSV with redacted JSON and a classification column (is_pii) indicating presence of PII.

**Files**
Filename	Description
detector_Samarth_K.py	Main Python script
iscp_pii_dataset.csv	Input CSV dataset
redacted_output_Samarth_K.csv	Output CSV with redacted data
