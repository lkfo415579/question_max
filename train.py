def active_megam():
	if nltk.megam._megam_bin is None:
		import os
		path = os.getcwd()
		nltk.config_megam(path+'/megam/megam-64.opt')

def test_maxent(algorithm,train_set,test_set):
	import time
	start_time = time.time()
	active_megam()
	print'%11s' % algorithm
	try:
		classifier
	except NameError:
		c_ex = True
	else:
		del classifier
	try:
		#global classifier
		classifier = nltk.classify.MaxentClassifier.train(
			train_set, algorithm, trace=1, max_iter=1000)
	except Exception as e:
		print 'Error: %r' % e
		return

	print 'This is most informative table'
	print classifier.show_most_informative_features(20)

	print 'Length of Testset :%d' % len(test_set)
	
	print 'Accuracy : ',
	print nltk.classify.accuracy(classifier, test_set)*100,
	print '%'
	'''
	for node in test_set[-5:]:
		pdist = classifier.prob_classify(node[0])
		print "prdist:"
		samples =  pdist.samples()
		for sample in samples:
			print sample
			print pdist.prob(sample)
		
		#for sample in pdist:
#			print sample
		print "correct"
		print node[1]
	'''
	print("---Total Used : %s Seconds ---" % (time.time() - start_time))
	
	return classifier
	# for featureset in test:
	#pdist = classifier.prob_classify(featureset)
	#print('%8.2f%6.2f' % (pdist.prob('x'), pdist.prob('y')) + end),
'''------------------------------------------------------------'''

import question

import nltk
nltk.usage(nltk.classify.ClassifierI)

featuresets = question.get_featureset()
import random
random.shuffle(featuresets)

print "Total len of featuresets : %s" % len(featuresets)
f_len = int(len(featuresets)*0.10)
train_set = featuresets[f_len:]
test_set = featuresets[:f_len]

print featuresets[0]

test_maxent('MEGAM',train_set,test_set)

