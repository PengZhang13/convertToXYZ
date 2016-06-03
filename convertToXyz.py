import pybel

def convertToXyz(xyz_file, output_xyz):
	f = open(xyz_file,'r')
	mol = []
	numMol = 0
	numLine = 0
	numAtom = []
	xyzSpc = []

	for line in f:
		if line[0] == '1' or line[0] == '2' or line[0] == '3' or line[0] == '4' or line[0] == '5' or line[0] == '6' or line[0] == '7' or line[0] == '8' or line[0] == '9':
			line = line.strip('\n')
			mol.append([])
			numMol += 1
			mol[numMol-1].append(line)

		else:
			line = line.strip('\n')
			mol[numMol-1].append(line)

	nameSpc = []
	for i in range(0,numMol):
		nameSpc.append(mol[i][0])
		xyzSpc.append([])
		numLine = len(mol[i])
		
		count = 0
		atomSymbol = 'A'
		for j in range(0,numLine):
			tempList = mol[i][j].split()
			if len(tempList) == 6 and tempList[0][0] != 'C' and mol[i][j].split()[0][0] != 'N':
				xyzSpc[i].append([])
				if tempList[1] == '1':
					atomSymbol = 'H'
				elif tempList[1] == '6':
					atomSymbol = 'C'
				elif tempList[1] == '8':
					atomSymbol = 'O'
				else:
					print 'ERROR! Bad Atomic Number! Not H/C/O!'
				
				xyzSpc[i][count].append(atomSymbol)
				xyzSpc[i][count].append(tempList[3])
				xyzSpc[i][count].append(tempList[4])
				xyzSpc[i][count].append(tempList[5])
				# print xyzSpc[i][count]
				count +=1
		numAtom.append(count)
	f.close()

	fw = open(output_xyz,'w')
	for i in range(0,numMol):
		fw.write(str(numAtom[i])+'\n')
		fw.write(nameSpc[i]+'\n')
		for j in range(0, len(xyzSpc[i])):
			tempstr = xyzSpc[i][j][0] + '  ' + xyzSpc[i][j][1] + '  ' + xyzSpc[i][j][2] + '  ' + xyzSpc[i][j][3] + '\n' 
			fw.write( tempstr )
		fw.write('\n')
	fw.close()

if __name__ == '__main__':
	convertToXyz('TrainingSet.log', 'output.txt')

