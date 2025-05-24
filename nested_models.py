from pydantic import BaseModel

class Address(BaseModel):

    city: str
    state: str
    pin: str

class Patient(BaseModel):

    name: str
    gender: str
    age: int
    address: Address

def create_patient(patient: Patient):
    print("Patient Created...")
    print(f"Name: {patient.name}, Age: {patient.age}, Address: {patient.address}")

if __name__ == "__main__":
    # Example patient data
    address_dict = {'city': 'delhi', 'state': 'delhi', 'pin': '110001'}
    address = Address(**address_dict)
    patient_dict = {'name': 'rohit', 'gender': 'male', 'age': 30, 'address': address}
    patient = Patient(**patient_dict)
    create_patient(patient)

# Output:
# Patient Created...
# Name: rohit, Age: 30, Address: city='delhi' state='delhi' pin='110001'