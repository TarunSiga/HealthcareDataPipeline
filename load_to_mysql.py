
import pandas as pd
import mysql.connector

def load_gold_to_mysql(patients_file, doctors_file, appointments_file):
    """Load Gold layer data into MySQL."""
    patients = pd.read_csv(patients_file)
    doctors = pd.read_csv(doctors_file)
    appointments = pd.read_csv(appointments_file)

    connection = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="admin",
        database="healthcare"
    )
    cursor = connection.cursor()

    # Insert Patients
    for _, row in patients.iterrows():
        cursor.execute(
            "INSERT INTO Patients (patient_dob, patient_gender) VALUES (%s, %s)",
            (row['Patient_DOB'], row['Patient_Gender'])
        )

    # Insert Doctors
    for _, row in doctors.iterrows():
        cursor.execute(
            "INSERT INTO Doctors (doctor_name, doctor_specialty, appointment_location) VALUES (%s, %s, %s)",
            (row['Doctor_Name'], row['Doctor_Specialty'], row['Appointment_Location'])
        )

    # Insert Appointments
    for _, row in appointments.iterrows():
        cursor.execute(
            "INSERT INTO Appointments (patient_id, doctor_id, appointment_datetime, reason_for_visit, note, follow_up) "
            "VALUES (%s, %s, %s, %s, %s, %s)",
            (row['patient_id'], row['doctor_id'], row['Appointment_DateTime'],
             row['Reason_for_Visit'], row['Note'], row['Follow_Up'] == "Yes")
        )

    connection.commit()
    cursor.close()
    connection.close()
    print("✅ Gold layer data successfully loaded into MySQL.")

if __name__ == "__main__":
    load_gold_to_mysql("gold_patients.csv", "gold_doctors.csv", "gold_appointments.csv")
