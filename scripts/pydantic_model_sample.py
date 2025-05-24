from pydantic import BaseModel, Field, EmailStr, AnyUrl
from typing import List, Dict, Optional, Annotated


class Patient(BaseModel):
    name: Annotated[str, Field(min_length=2, max_length=50, description="Full name of the patient (2-50 characters)")]
    age: int = Field(gt=0, lt=120)
    email: EmailStr
    weight: Annotated[float, Field(gt=0, strict=True)]
    married: Annotated[bool, Field(default=None, description="Is the patient married?")]
    linkedIn_url: Optional[AnyUrl]
    contact_details: Dict[str, str]
    allergies: Annotated[Optional[List[str]], Field(default=None, max_length=5, description="List of allergies, if any")]


# Example usage
def create_patient(patient: Patient):
    print("Patient Created...")
    print(f"Name: {patient.name}, Age: {patient.age}, Email: {patient.email}")


if __name__ == "__main__":
    # Example patient data
    patient_data = {
        "name": "rohit",
        "age": 30,
        "email": "example@gmail.com",
        "weight": 70.5,
        "linkedIn_url": "https://www.linkedin.com/in/example",
        "contact_details": {'phone': '123445678'},
        "allergies": ["peanuts", "shellfish"]
    }

    # Create a Patient instance
    patient = Patient(**patient_data)

    # Call the function to create a patient
    create_patient(patient)

# Output:
# Patient Created...
# Name: rohit, Age: 30, Email: ['peanuts', 'shellfish']