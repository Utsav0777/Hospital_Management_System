def admit_patient(patient_id, ward):
    print("Patient", patient_id, "admitted to", ward)


def discharge_patient(patient_id):
    print("Patient", patient_id, "discharged")


def calculate_bill(days, rate=1000):
    bill = days * rate
    print("Bill = Rs.", bill)
    return bill
