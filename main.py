import brisk

matrix =  brisk.get_features('obj.png')

print 'length of matrix : ',len(matrix)
print 'breadth of matrix : ',len(matrix[0])