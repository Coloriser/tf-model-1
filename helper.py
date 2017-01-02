def to_single_dimensional_array(extracted_features):
	one_dim_arr = []

	for elem in extracted_features:

		# print "one d :",one_dim_arr
		# print "elem : ",elem
		one_dim_arr = one_dim_arr + list(elem)

	return one_dim_arr