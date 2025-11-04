from hw5 import Patient

def test_add_test_correct():
    p = Patient("Majo", ["cough"])
    p.add_test("covid", True)
    
    assert hasattr(p, "tests")
    assert p.tests.get("covid") is True

def test_has_covid_with_test_positive():
    p = Patient("Majo", ["cough"])
    p.add_test("covid", True)
    
    prob = p.has_covid()
    assert prob == 0.99

    def test_has_covid_with_test_positive():
    p = Patient("Majo", ["cough"])
    p.add_test("covid", False)
    
    prob = p.has_covid()
    assert prob == 0.01

def test_has_covid_no_test_some_symptoms():
    p = Patient("Majo", ["fever", "headache"])
    result = p.has_covid()
    # Base 0.05 + 0.1 for 'fever' only = 0.15
    assert result == 0.15