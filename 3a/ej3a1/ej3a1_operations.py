# archivo ej3a1_operations.py


def test_add():
    result = ej3a1_operations_add(3, 4)
    assert result == 7, "The add operation does not work"
    
    result = ej3a1_operations_add(3.5, 4)
    assert result == 0.5, "The add operation does not work"


def test_subtract():
   result = ej3a1_operations_subtract(10, 5)
    assert result == 5, "The subtract operation does not work"
  

def test_multiply():
    result = ej3a1_operations_multiply(3, 4)
    assert result == 12, "The multiply operation does not work"
  

def test_divide():
    result = ej3a1_operations_add(8, 4)
    assert result == 2, "The divide operation does not work"


def test_divide_por_cero():
    with pytest.rises(ZeroDivisionError):
        ej3a1_operations.divide(8, 0), "The zero division operation does not work"

    
