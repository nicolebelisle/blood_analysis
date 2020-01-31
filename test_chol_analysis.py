def test_HDL_analysis():
	from interface import HDL_analysis
	answer = HDL_analysis(80)
	expected = "Normal"
	assert answer == expected

def test_HDL_analysis_b1():
	from chol_analysis import HDL_analysis
	answer = HDL_analysis(40)
	expected = "Borderline Low"
	assert answer == expected

def test_LDL_analysis
	from chol_analysis import LDL_analysis
	answer = LDL_analysis(165)
	expected = "High"
	assert answer == expected
