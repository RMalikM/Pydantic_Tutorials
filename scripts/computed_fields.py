from pydantic import BaseModel, EmailStr, computed_field
from typing import List, Dict


class Patient(BaseModel):
    name: str
    age: int
    email: EmailStr
    weight: float
    height: float
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]

    @computed_field
    @property
    def bmi(self) -> float:
        """Calculate Body Mass Index (BMI) based on weight and height."""
        bmi = self.weight / (self.height ** 2)
        return round(bmi, 2)
    
def create_patient(patient: Patient):
    print("Patient Created...")
    print(f"Name: {patient.name}, Age: {patient.age}, Email: {patient.allergies}, BMI: {patient.bmi}")


if __name__ == "__main__":
    # Example patient data
    patient_data = {
        "name": "rohit",
        "age": 65,      # Set it to below 60 to see the model validation effect
        "email": "example@sbi.com",
        "weight": 70.5, # Weight in kg
        "height": 1.75, # Height in meters
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
# Name: rohit, Age: 65, Email: ['peanuts', 'shellfish'], BMI: 23.02