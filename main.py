import brisk
import chromaEx as CE

matrix =  brisk.get_features('col.jpg')
chroma = CE.extractA('col.jpg')

print chroma

print 'length of matrix : ',len(matrix)
print 'breadth of matrix : ',len(matrix[0])