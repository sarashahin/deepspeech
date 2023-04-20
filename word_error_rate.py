import numpy as np 

def word_error_rate(string1, string2):
	"""
	Simple implementation of the Levenstein Distence and word error rate (WER)
	Distance computed with iterative matrix
	WER computed using formula from Levenshtein, Vladimir I. (February 1966). "Binary codes capable of correcting 
	deletions, insertions, and reversals".
	Python implementation of the levenshtein distance computation:
	input: string1: string
		   string2: string
    output: int
	"""
	if string1 == string2:
		return 0 
	else:

		dis = np.zeros([len(string1)+1, len(string2)+1], dtype=int)

		for i in range(1, len(string1)+1):
			dis[i, 0] = i

		for j in range(1, len(string2)+1):
			dis[0, j] = j

		for j in range(1, len(string2)+1):
			for i in range(1, len(string1)+1):


				if string1[i-1] == string2[j-1]:
					substituted_cost = 0
				else:
					substituted_cost = 1

				updatings = dict(a=dis[i-1, j] + 1,b=dis[i, j-1] + 1,c=dis[i-1, j-1] + substituted_cost)
				key_min = min(updatings.keys(), key=(lambda k: updatings[k]))
				dis[i, j] = updatings[key_min]
				
		WER = (dis[len(string1), len(string2)] / max(len(string1), len(string2))) * 100
		WERAcc = 100 - WER
	return dis[len(string1), len(string2)], WER, WERAcc

# distance, WER, WERAcc = word_error_rate('Please, I have lost my suitcase.','please i have lost my suitcase')
# distance, WER, WERAcc = word_error_rate('Por favor, he perdido mi maleta.','por favor he perdido mi maleta')
# distance, WER, WERAcc = word_error_rate("Dove e' il bancone?",'dove er il bancone')
# distance, WER, WERAcc = word_error_rate('I am a student!','i am a student')
# distance, WER, WERAcc = word_error_rate('Please, sit down.','please sit down')
distance, WER, WERAcc = word_error_rate('Dove sono i ristoranti e i negozi?','dove sone ristorantie nedozi')


print(f"Levenstein distance is: {distance}")
print(f"Word error rate is: {WER}%")
print(F"Word Accuracy is: {WERAcc}%")
