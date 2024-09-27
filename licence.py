class LicensePlate:
    def __init__(self, plate_id, registration_date, owner):
        self.plate_id = plate_id
        self.registration_date = registration_date
        self.owner = owner

class LicensePlateRepository:
    def __init__(self):
        self.plates = {}

    def add_plate(self, plate):
        self.plates[plate.plate_id] = plate

    def get_plate(self, plate_id):
        return self.plates.get(plate_id)

    def update_plate(self, plate_id, **kwargs):
        plate = self.get_plate(plate_id)
        if plate:
            for key, value in kwargs.items():
                setattr(plate, key, value)

    def delete_plate(self, plate_id):
        if plate_id in self.plates:
            del self.plates[plate_id]

class RecognitionLog:
    def __init__(self):
        self.recognitions = {}

    def log_recognition(self, recognition_id, plate_id):
        self.recognitions[recognition_id] = plate_id

    def get_recognition(self, recognition_id):
        return self.recognitions.get(recognition_id)

class ALPRSystem:
    def __init__(self, plate_repo, recognition_log):
        self.plate_repo = plate_repo
        self.recognition_log = recognition_log

    def recognize_license_plate(self, plate_id):
        # Simulate license plate recognition
        plate = self.plate_repo.get_plate(plate_id)
        if plate:
            print(f"Recognized license plate: {plate_id}, Owner: {plate.owner}")
        else:
            print(f"License plate {plate_id} not found.")

    def log_recognitions(self, recognition_id, plate_id):
        self.recognition_log.log_recognition(recognition_id, plate_id)
        print(f"Logged recognition ID: {recognition_id} for plate {plate_id}")


### Unit Testing with unittest


import unittest

class TestALPRSystem(unittest.TestCase):
    def test_license_plate_operations(self):
        repo = LicensePlateRepository()
        plate = LicensePlate("XYZ123", "2023-05-01", "John Doe")
        
        # Test Create
        repo.add_plate(plate)
        self.assertIn("XYZ123", repo.plates)
        
        # Test Read
        self.assertEqual(repo.get_plate("XYZ123"), plate)
        
        # Test Update
        repo.update_plate("XYZ123", owner="Jane Doe")
        self.assertEqual(repo.get_plate("XYZ123").owner, "Jane Doe")
        
        # Test Delete
        repo.delete_plate("XYZ123")
        self.assertNotIn("XYZ123", repo.plates)

    def test_recognitions_logging(self):
        log = RecognitionLog()
        
        # Test Log Recognition
        log.log_recognition("1", "XYZ123")
        self.assertEqual(log.get_recognition("1"), "XYZ123")

    def test_alpr_system(self):
        repo = LicensePlateRepository()
        log = RecognitionLog()
        alpr = ALPRSystem(repo, log)
        
        plate = LicensePlate("XYZ123", "2023-05-01", "John Doe")
        repo.add_plate(plate)
        
        # Test Recognize License Plate
        alpr.recognize_license_plate("XYZ123")  # Should print recognized plate
        alpr.recognize_license_plate("ABC456")  # Should print not found
        
        # Test Log Recognition
        alpr.log_recognitions("1", "XYZ123")
        self.assertEqual(log.get_recognition("1"), "XYZ123")

if __name__ == "__main__":
    unittest.main()
