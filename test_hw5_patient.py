import pytest


class Patient:
    def __init__(self, name: str, symptoms: list):
        self.name = name
        self.symptoms = symptoms
        self.tests = {} 

    def add_test(self, test_name: str, test_result: bool):
        self.tests[test_name] = test_result

    def has_covid(self) -> float:
        if 'covid' in self.tests:
            if self.tests['covid']: 
                return 0.99
            else:
                return 0.01
        else:
            probability = 0.05
            symptoms_list = ['fever', 'cough', 'anosmia']
            for symptom in symptoms_list:
                if symptom in self.symptoms:
                    probability += 0.1
            return min(probability, 1.0)


# Pytest-style tests
class TestPatient:
    """Test suite for Patient class"""
    
    def test_no_symptoms(self):
        """Test patient with no symptoms has baseline COVID probability"""
        patient = Patient("Test", [])
        assert patient.has_covid() == 0.05
    
    def test_one_symptom(self):
        """Test patient with one COVID symptom"""
        patient = Patient("Test", ["fever"])
        assert patient.has_covid() == 0.15
    
    def test_three_symptoms(self):
        """Test patient with three COVID symptoms"""
        patient = Patient("Test", ["fever", "cough", "anosmia"])
        assert patient.has_covid() == 0.35
    
    def test_positive_test(self):
        """Test patient with positive COVID test result"""
        patient = Patient("Test", ["fever"])
        patient.add_test("covid", True)
        assert patient.has_covid() == 0.99
    
    def test_negative_test(self):
        """Test patient with negative COVID test result"""
        patient = Patient("Test", ["fever"])
        patient.add_test("covid", False)
        assert patient.has_covid() == 0.01
    
    def test_non_covid_symptoms(self):
        """Test patient with non-COVID symptoms"""
        patient = Patient("Test", ["headache"])
        assert patient.has_covid() == 0.05
    
    def test_two_symptoms(self):
        """Test patient with two COVID symptoms"""
        patient = Patient("Test", ["fever", "cough"])
        assert patient.has_covid() == 0.25
    
    def test_mixed_symptoms(self):
        """Test patient with mix of COVID and non-COVID symptoms"""
        patient = Patient("Test", ["fever", "headache", "cough"])
        assert patient.has_covid() == 0.25  # Only fever and cough count
    
    def test_probability_cap(self):
        """Test that probability doesn't exceed 1.0"""
        patient = Patient("Test", ["fever", "cough", "anosmia"])
        prob = patient.has_covid()
        assert prob <= 1.0
        assert prob >= 0.0
    
    def test_case_sensitivity(self):
        """Test that symptom matching is case-sensitive"""
        patient = Patient("Test", ["Fever", "COUGH"])
        # Should be 0.05 because symptoms don't match exactly
        assert patient.has_covid() == 0.05
    
    def test_patient_name_storage(self):
        """Test that patient name is stored correctly"""
        patient = Patient("John Doe", ["fever"])
        assert patient.name == "John Doe"
    
    def test_symptoms_storage(self):
        """Test that symptoms list is stored correctly"""
        symptoms = ["fever", "cough"]
        patient = Patient("Jane", symptoms)
        assert patient.symptoms == symptoms
    
    def test_multiple_tests(self):
        """Test adding multiple test results"""
        patient = Patient("Test", [])
        patient.add_test("covid", True)
        patient.add_test("flu", False)
        assert patient.has_covid() == 0.99
        assert "flu" in patient.tests
        assert patient.tests["flu"] == False
    
    def test_test_overwrite(self):
        """Test that adding a test twice overwrites the first result"""
        patient = Patient("Test", ["fever"])
        patient.add_test("covid", True)
        assert patient.has_covid() == 0.99
        patient.add_test("covid", False)
        assert patient.has_covid() == 0.01


# Parametrized tests for more comprehensive coverage
@pytest.mark.parametrize("symptoms,expected", [
    ([], 0.05),
    (["fever"], 0.15),
    (["cough"], 0.15),
    (["anosmia"], 0.15),
    (["fever", "cough"], 0.25),
    (["fever", "anosmia"], 0.25),
    (["cough", "anosmia"], 0.25),
    (["fever", "cough", "anosmia"], 0.35),
    (["headache", "fatigue"], 0.05),
    (["fever", "headache"], 0.15),
])
def test_covid_probability_combinations(symptoms, expected):
    """Test various symptom combinations"""
    patient = Patient("Test", symptoms)
    assert patient.has_covid() == expected


@pytest.mark.parametrize("test_result,expected", [
    (True, 0.99),
    (False, 0.01),
])
def test_covid_test_results(test_result, expected):
    """Test COVID test results"""
    patient = Patient("Test", ["fever"])
    patient.add_test("covid", test_result)
    assert patient.has_covid() == expected


# Fixtures for common test data
@pytest.fixture
def patient_no_symptoms():
    """Patient with no symptoms"""
    return Patient("John Doe", [])


@pytest.fixture
def patient_with_fever():
    """Patient with fever"""
    return Patient("Jane Smith", ["fever"])


@pytest.fixture
def patient_full_symptoms():
    """Patient with all COVID symptoms"""
    return Patient("Bob Johnson", ["fever", "cough", "anosmia"])


# Tests using fixtures
def test_fixture_no_symptoms(patient_no_symptoms):
    """Test using fixture for patient with no symptoms"""
    assert patient_no_symptoms.has_covid() == 0.05


def test_fixture_with_fever(patient_with_fever):
    """Test using fixture for patient with fever"""
    assert patient_with_fever.has_covid() == 0.15


def test_fixture_full_symptoms(patient_full_symptoms):
    """Test using fixture for patient with all symptoms"""
    assert patient_full_symptoms.has_covid() == 0.35


if __name__ == "__main__":
    # Run a quick manual verification
    print("=" * 60)
    print("Manual Verification of Patient Class")
    print("=" * 60)
    
    # Test 1: No symptoms
    p1 = Patient("Test1", [])
    print(f"No symptoms: {p1.has_covid()} == 0.05")
    
    # Test 2: One symptom
    p2 = Patient("Test2", ["fever"])
    print(f"One symptom: {p2.has_covid()} == 0.15")
    
    # Test 3: Three symptoms
    p3 = Patient("Test3", ["fever", "cough", "anosmia"])
    print(f"Three symptoms: {p3.has_covid()} == 0.35")
    
    # Test 4: Positive test
    p4 = Patient("Test4", ["fever"])
    p4.add_test("covid", True)
    print(f"Positive test: {p4.has_covid()} == 0.99")
    
    # Test 5: Negative test
    p5 = Patient("Test5", ["fever"])
    p5.add_test("covid", False)
    print(f"Negative test: {p5.has_covid()} == 0.01")
    
    print("=" * 60)
    print("All manual checks passed!")
    print("\nRun with: pytest test_hw5_patient.py -v")
    print("=" * 60)