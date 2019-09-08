from multiprocessing import Pool

def squareNumber(n):
	return n ** 100

def calculateParallel(numbers, threads=2):
	pool = Pool(threads)
	results = pool.map(squareNumber, numbers)
	pool.close()
	pool.join()
	return results

if __name__ == '__main__':
	numbers = range(100000)
	squaredNumbers = calculateParallel(numbers,4)
	#for n in squaredNumbers:
		#print n
