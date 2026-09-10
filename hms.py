patients = ["Rahul", "Priya", "Amit"]


def admit_patient(patient_id, ward):
    print("Patient", patient_id, "admitted to", ward)
def calculate_bill(days, rate=1000):
    bill = days * rate
    print("Bill = Rs.", bill)
    return bill


def search_patient(name):
    if name in patients:
        print(name, "is registered")
    else:
        print(name, "not found")
