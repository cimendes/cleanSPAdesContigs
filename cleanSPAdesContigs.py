import sys

def writeOutFile(fastaFile, list_sequences, outputFile):
	writer = open(outputFile, 'wt')

	number_sequences = 0
	number_bases = 0
	seqHeader = ''
	seqSequence = ''
	with open(fastaFile, 'rtU') as lines:
		for line in lines:
			line = line.splitlines()[0]
			if len(line) > 0:
				if line[0] == '>':
					if seqHeader != '':
						sequenced_found = False

						if seqHeader[1:] in list_sequences:
							# First search
							sequenced_found = True
						elif seqHeader[1:].split()[0] in list_sequences:
							# Second search
							sequenced_found = True

						if sequenced_found:
							writer.write(seqHeader + '\n')
							writer.write(seqSequence + '\n')
							writer.flush()
							number_bases = number_bases + len(seqSequence)
							number_sequences += 1

					seqHeader = ''
					seqSequence = ''
					seqHeader = line
				else:
					seqSequence = seqSequence + line

		sequenced_found = False

		if seqHeader[1:] in list_sequences:
			# First search
			sequenced_found = True
		elif seqHeader[1:].split()[0] in list_sequences:
			# Second search
			sequenced_found = True

		if sequenced_found:
			writer.write(seqHeader + '\n')
			writer.write(seqSequence + '\n')
			writer.flush()
			number_bases = number_bases + len(seqSequence)
			number_sequences += 1

	writer.close()

	return number_sequences, number_bases


def getSequences(fastaFile, sequencesListFile, outputFile):

	number_sequences, number_bases = writeOutFile(fastaFile, sequencesListFile, outputFile)

	return outputFile, number_sequences, number_bases

def getHeaders(filename):

	headers_to_remove=[]
	headers_to_keep=[]
	size=0
	with open(filename, "r") as fastaFile:
		for line in fastaFile:
			if line.startswith('>'):
				items=line.split('_')
				if int(items[4])<200 or float(items[6])<5:
					headers_to_remove.append(line)
					length=items[4]
					size+=int(length)
				else:
					line=line.split('>')
					line=line[1].strip()
					headers_to_keep.append(line)

	print ('Number of contigs to remove: %s') % (str(len(headers_to_remove)))
	print('Total length to remove: %s') % (str(size))
	print ('Number of contigs to keep: %s') % (str(len(headers_to_keep)))

	return headers_to_keep

def main():
	fastaFile=sys.argv[1]
	outputFile=sys.argv[2]

	sequencesListFile=getHeaders(fastaFile)

	getSequences(fastaFile, sequencesListFile, outputFile)

if __name__ == '__main__':
	main()