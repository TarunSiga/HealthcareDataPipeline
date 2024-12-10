
import pandas as pd
from dateutil import parser
import calendar


def clean_silver_layer(file_path):
    """Clean and validate the Bronze layer data for the Silver layer."""
    df = pd.read_csv(file_path)

    # Rename Columns for consistency
    df.rename(columns={"Patient Name": "Patient_Name", "Patint DOB": "Patient_DOB", "Patient Gendr": "Patient_Gender", 
                       "Appointment date time": "Appointment_DateTime", "Doctor name": "Doctor_Name"
                       , "Doctor specialty": "Doctor_Specialty"
                       , "Appointment location": "Appointment_Location"
                       , "Reason for visit": "Reason_for_Visit"
                       , "Follow up": "Follow_Up"}, inplace=True)
    
   
    

    # Cleaning operations
    df['Patient_Name'] = df['Patient_Name'].str.strip().str.title().fillna("Unknown")
   
    # Standardize the Patient_DOB column
    def standardize_date(dob):
        """Convert date to MM-DD-YYYY format or return 'Unknown' if invalid."""
        try:
            return parser.parse(str(dob)).strftime('%m-%d-%Y')
        except (parser.ParserError, ValueError, TypeError):
            return "Unknown"

    df['Patient_DOB'] = df['Patient_DOB'].apply(standardize_date)

    df['Patient_Gender'] = df['Patient_Gender'].str.strip().str.lower().map({
            'm': 'Male',
            'male': 'Male',
            'f': 'Female',
            'female': 'Female'
        }).fillna("Unknown")
    

    def standardize_datetime(datetime_str):
        """Standardize the appointment date-time format (MM-DD-YYYY HH:MM:SS) or return 'Unknown'."""
        if not datetime_str or datetime_str == 'nan' or datetime_str == '':  # Check for empty values
            return "Unknown"
    
        try:
            # Try parsing the datetime
            parsed_datetime = parser.parse(str(datetime_str))
        
            # Check if time is missing (0 hours, 0 minutes, 0 seconds)
            if parsed_datetime.hour == 0 and parsed_datetime.minute == 0 and parsed_datetime.second == 0:
                return parsed_datetime.strftime('%m-%d-%Y') + " 00:00:00"
        
            # If the datetime is valid, format it to MM-DD-YYYY HH:MM:SS
            return parsed_datetime.strftime('%m-%d-%Y %H:%M:%S')
        except (parser.ParserError, ValueError, TypeError):
            # If parsing fails or the datetime is invalid, return 'Unknown'
            return "Unknown"

    # Standardize the Appointment_DateTime column
    df['Appointment_DateTime'] = df['Appointment_DateTime'].apply(lambda x: standardize_date(x))

    df['Reason_for_Visit'] = df['Reason_for_Visit'].fillna("N/A")
    df['Note'] = df['Note'].fillna("N/A")
    df['Follow_Up'] = df['Follow_Up'].str.strip().str.capitalize()

   # df['Appointment_DateTime'] = pd.to_datetime(df['Appointment_DateTime'], errors='coerce')

    df.drop_duplicates(inplace=True)
    df.to_csv("silver_cleaned_data.csv", index=False)

    print("✅ Data successfully cleaned into the Silver layer.")
    return df

if __name__ == "__main__":
    clean_silver_layer("bronze_raw_data.csv")
