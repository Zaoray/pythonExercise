from numpy import *

def loadSimpData():
	datMat = matrix([[1. , 2.1],
		[2. , 1.1],
		[1.3, 1. ],
		[1. , 1. ],
		[2. , 1. ]])
	classLabels = [1.0, 1.0, -1.0, -1.0, 1.0]
	return datMat, classLabels
def stumpClassify(dataMatrix, dimen, threshVal, threshIneq):
	retArray = ones((shape(dataMatrix)[0], 1))
	if threshIneq == 'lt':
		retArray[dataMatrix[:, dimen] <= threshVal] = -1.0
	else:
		retArray[dataMatrix[:, dimen] > threshVal] = -1.0
	return retArray

def buildStump(dataArr, classLabels, D):
	dataMatrix = mat(dataArr); labelMat = mat(classLabels).T
	m, n = shape(dataMatrix)
	numSteps = 10.0; bestStump = {}; bestClasEst = mat(zeros((m,1)))
	minError = inf
	for i in range(n):
		rangeMin = dataMatrix[:,i].min(); rangeMax = dataMatrix[:,i].max();
		stepSize = (rangeMax - rangeMin) / numSteps
		for i in range(-1, int(numSteps) + 1):
			for inequal in ['lt', 'gt']:
				threshVal = (rangeMin + float(j) * stepSize)
				predictedVals = \
						stumpClassify(dataMatrix, i, threshVal, inequal)
				errArr = mat(ones((m,1)))
				errArr[predictedVals == labelMat] = 0
				weightedError = D.T * errArr
				#print ""