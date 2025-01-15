import pytest
# pytest
# Function names must start with "test" so when running pytest it is recognized
# script name does not matter what name it has
# No main function is needed

def invertFunction(array:str):
    if array == None:
        return ""
    array = array [::-1]
    return array

@pytest.mark.parametrize("testcase, expected", [
    ("10", "01"),  # Prueba 1
    ("Hola Mundo Pruebas", "sabeurP odnuM aloH"),    # Prueba 2
    ("", ""), # Prueba 3
    (None, ""),       # Prueba 4 con error
    ("_5", "5_"),  # Prueba 5
    ("AA", "AA"),  # Prueba 6
    ("0sO", "Os0")  # Last test without the colon

])

def testFunction(testcase, expected):
    assert invertFunction(testcase) == expected


#any code is needed in main
#if __name__ == "__main__":
#    pass
