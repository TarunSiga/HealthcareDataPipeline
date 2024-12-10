
import pandas as pd

def transform_gold_layer(file_path):
    """Transform the Silver layer data into normalized tables for the Gold layer."""
    df = pd.read_csv(file_path)

    # Patients table
    patients = df[['Patient_Name', 'Patient_DOB', 'Patient_Gender']].drop_duplicates().reset_index(drop=True)
    patients['patient_id'] = range(1, len(patients) + 1)
    patients.to_csv("gold_patients.csv", index=False)

    # Doctors table
    doctors = df[['Doctor_Name', 'Doctor_Specialty', 'Appointment_Location']].drop_duplicates().reset_index(drop=True)
    doctors['doctor_id'] = range(1, len(doctors) + 1)
    doctors.to_csv("gold_doctors.csv", index=False)

    # Appointments table
    appointments = df.merge(
        patients, on=['Patient_DOB', 'Patient_Gender'], how='left'
    ).merge(
        doctors, on=['Doctor_Name', 'Doctor_Specialty', 'Appointment_Location'], how='left'
    )
    appointments = appointments[['patient_id', 'doctor_id', 'Appointment_DateTime',
                                  'Reason_for_Visit', 'Note', 'Follow_Up']]
    appointments['appointment_id'] = range(1, len(appointments) + 1)
    appointments.to_csv("gold_appointments.csv", index=False)

    print("✅ Data successfully transformed into the Gold layer.")
    return patients, doctors, appointments

if __name__ == "__main__":
    transform_gold_layer("silver_cleaned_data.csv")
