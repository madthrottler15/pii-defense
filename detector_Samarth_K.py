import re
import json
import pandas as pd
import sys


def mask_phone(val):
    return val[:2] + "XXXXXX" + val[-2:]

def mask_aadhar(val):
    return val[:4] + " XXXX XXXX"

def mask_passport(val):
    return val[0] + "XXXXXXX"

def mask_upi(val):
    if "@" in val:
        u, d = val.split("@", 1)
        return u[:2] + "XX@" + d
    return val

def mask_name(val):
    parts = val.split()
    return " ".join([p[0] + "XXX" for p in parts])

def mask_email(val):
    u, d = val.split("@", 1)
    return u[:2] + "XXX@" + d

def detect_and_redact(record):
    is_pii = False
    try:
        data = json.loads(record)
    except:
        return record, False

    if "phone" in data and re.fullmatch(r"\d{10}", str(data["phone"])):
        data["phone"] = mask_phone(str(data["phone"]))
        is_pii = True

    if "aadhar" in data and re.fullmatch(r"\d{12}", str(data["aadhar"])):
        data["aadhar"] = mask_aadhar(str(data["aadhar"]))
        is_pii = True

    if "passport" in data and re.fullmatch(r"[A-PR-WYa-pr-wy][1-9]\d{6}", str(data["passport"])):
        data["passport"] = mask_passport(str(data["passport"]))
        is_pii = True

    if "upi_id" in data and re.match(r".+@.+", str(data["upi_id"])):
        data["upi_id"] = mask_upi(str(data["upi_id"]))
        is_pii = True

    combo_fields = ["name", "email", "address", "ip_address"]
    found = [f for f in combo_fields if f in data and data[f]]

    if len(found) >= 2:
        is_pii = True
        if "name" in data:
            data["name"] = mask_name(str(data["name"])) 
        if "email" in data:
            data["email"] = mask_email(str(data["email"])) 
        if "address" in data:
            data["address"] = "XX..."
        if "ip_address" in data:
            data["ip_address"] = "XXX.XXX.XXX.XXX"

    return json.dumps(data), is_pii

def main(input_file):
    df = pd.read_csv(input_file)
    output = []

    for _, row in df.iterrows():
        redacted_json, is_pii = detect_and_redact(row["data_json"])
        output.append([row["record_id"], redacted_json, is_pii])

    out_df = pd.DataFrame(output, columns=["record_id", "redacted_data_json", "is_pii"])
    out_file = "redacted_output_Samarth_K.csv"
    out_df.to_csv(out_file, index=False)
    print(f"Output saved to {out_file}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 detector_Samarth_K.py iscp_pii_dataset.csv")
    else:
        main(sys.argv[1])
