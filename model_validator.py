from pydantic import BaseModel, EmailStr, model_validator
from typing import List, Dict


class Patient(BaseModel):
    name: str
    age: int
    email: EmailStr
    weight: float
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]

    @model_validator(mode='after')
    def validate_emergency_contact(cls, model):
        if model.age > 60 and 'emergency_contact' not in model.contact_details:
            raise ValueError("Emergency contact is required in contact details for patients over 60 years old.")
        return model
    
def create_patient(patient: Patient):
    print("Patient Created...")
    print(f"Name: {patient.name}, Age: {patient.age}, Email: {patient.allergies}")


if __name__ == "__main__":
    # Example patient data
    patient_data = {
        "name": "rohit",
        "age": 65,      # Set it to below 60 to see the model validation effect
        "email": "example@sbi.com",
        "weight": 70.5,
        "married": True,
        "allergies": ["peanuts", "shellfish"],
        "contact_details": {'phone': '123445678', 'emergency_contact': '987654321'}
    }

    # Create a Patient instance
    patient = Patient(**patient_data)

    # Call the function to create a patient
    create_patient(patient)

# Output:
# Patient Created...
# Name: rohit, Age: 65, Email: ['peanuts', 'shellfish']