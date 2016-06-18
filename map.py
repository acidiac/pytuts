def sft_to_sqm(val):
	'''
		square feet area into square meters
	'''
	return (val * 0.09290)

area_sft = [23,34,45,67,73,11,89,113]

area_sqm = list(map(sft_to_sqm, area_sft))

print(area_sqm)

