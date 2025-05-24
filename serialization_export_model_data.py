from pydantic import BaseModel

class Address(BaseModel):

    city: str
    state: str
    pin: str

class Patient(BaseModel):

    name: str
    gender: str = 'Male'
    age: int
    address: Address

def create_patient(patient: Patient):
    print("Patient Created...")
    print(f"Name: {patient.name}, Age: {patient.age}, Address: {patient.address}")

if __name__ == "__main__":
    # Example patient data
    address_dict = {'city': 'delhi', 'state': 'delhi', 'pin': '110001'}
    address = Address(**address_dict)
    patient_dict = {'name': 'rohit', 'age': 30, 'address': address}
    patient = Patient(**patient_dict)

    # Exporting model data to a dictionary
    temp1 = patient.model_dump(exclude_unset=True)
    print(temp1, type(temp1))

    # Exporting model data to a JSON string
    temp2 = patient.model_dump_json(exclude={'address'})
    print(temp2, type(temp2))

# Output 1:
# {'name': 'rohit', 'age': 30, 'address': {'city': 'delhi', 'state': 'delhi', 'pin': '110001'}} <class 'dict'>

# Output 2:
# {"name":"rohit","gender":"Male","age":30} <class 'str'>