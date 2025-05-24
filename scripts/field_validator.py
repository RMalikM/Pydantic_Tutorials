from pydantic import BaseModel, EmailStr, field_validator
from typing import List, Dict


class Patient(BaseModel):
    name: str
    age: int
    email: EmailStr
    weight: float
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]

    # Field validators Examples: Custom data validation and transformation of fields
    @field_validator('email')
    @classmethod
    def validate_email(cls, value):
        valid_domains = ['hdfc.com', 'icici.com', 'sbi.com']
        domain_name = value.split('@')[-1]
        if domain_name not in valid_domains:
            raise ValueError(f"Email domain '{domain_name}' is not allowed. Allowed domains: {', '.join(valid_domains)}")
        return value
    
    @field_validator('name')
    @classmethod
    def transform_name(cls, value):     # Field validator can be used to transform the field value
        return value.upper()
    
    @field_validator('age', mode='after')  # validation -> type coercion
    @classmethod
    def validate_age(cls, value):
        if 0 < value < 100:
            return value
        else:
            raise ValueError('Age should be in between 0 and 100')


def create_patient(patient: Patient):
    print("Patient Created...")
    print(f"Name: {patient.name}, Age: {patient.age}, Email: {patient.allergies}")


if __name__ == "__main__":
    # Example patient data
    patient_data = {
        "name": "rohit",
        "age": 30,      # Change it to '30' to see the validation mode effect
        "email": "example@sbi.com",
        "weight": 70.5,
        "married": True,
        "allergies": ["peanuts", "shellfish"],
        "contact_details": {'phone': '123445678'}
    }

    # Create a Patient instance
    patient = Patient(**patient_data)

    # Call the function to create a patient
    create_patient(patient)

# Output:
# Patient Created...
# Name: ROHIT, Age: 30, Email: ['peanuts', 'shellfish']