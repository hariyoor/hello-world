from unnecessary_math import multiply
 
def test_numbers_3_4():
    assert multiply(3,4) == 12 
 
def test_strings_a_3():
    assert multiply('a',3) == 'aaa' 

def test_number_5_6():
	assert multiply(5,6) == 30

def test_number_10_23():
	assert multiply(10,23) == 230
	