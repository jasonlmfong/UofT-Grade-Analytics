def find_gpa(float):
	"""gives the gpa according to uoft scale"""
	if 85 <= float <= 100:
		return 4
	if 80 <= float <= 84:
		return 3.7
	if 77 <= float <= 79:
		return 3.3
	if 73 <= float <= 76:
		return 3
	if 70 <= float <= 72:
		return 2.7
	if 67 <= float <= 69:
		return 2.3
	if 63 <= float <= 66:
		return 2
	if 60 <= float <= 62:
		return 1.7
	if 57 <= float <= 59:
		return 1.3
	if 53 <= float <= 56:
		return 1
	if 50 <= float <= 52:
		return 0.7
	if 0 <= float <= 49:
		return 0
