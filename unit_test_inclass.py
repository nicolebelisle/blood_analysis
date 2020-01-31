#in-class finding value of y on slope 


def test_return_slope():
	from value_on_slope import return_slope
	answer = test_return_slope()
	expected = (y2 - y1) / (x2 - x1)
	assert answer == expected


def test_return_y():
	from value_on_slope import return_y
	answer = test_retun_y()
	assert answer == expected
	
