import sys
try:
	choice = sys.argv[1]
	if choice == "1":
		choice = 1
except:
	choice = 1
print "Type of %s" % choice
def count_match_dict(target, list):
	try:
		#candidate_list = my_dict[source]
		#print list
		#print 'list word : %s ' % target
		for list_word in list:
			if target == list_word:
				return 1
		return 0
			# print '-target- ' + target +' -word- ' + word + ' -source- ' + source
		#
	except KeyError:
		return 0
		
def get_featureset():
	import xml.etree.cElementTree as ET
	tree = ET.ElementTree(file='data/train.xml')

	root = tree.getroot()
	#for child_of_root in root:
	#	print child_of_root.tag, child_of_root.attrib
	#got xml data,trainning data.
	#creating featureset

	featureset = []

	def gender_features(data):
		featureset = []
		features = {}
		features['QCATEGORY'] = data.attrib['QCATEGORY']
		#features['QGOLD_YN'] = data.attrib['QGOLD_YN']
		
		if choice == 1:
			if data.attrib['QTYPE'] == "YES_NO":
				return None
		else:
			if data.attrib['QTYPE'] == "GENERAL":
				return None
		
		#features['comments'] = []
		QSubject = data[0].text.split()
		#features['QSubject'] = tuple(QSubject.text.split())
		QBody = data[1].text.split()
		#features['QBody'] = tuple(QBody.text.split())
		
		del data[0]
		del data[0]
		for node in data:
			#print node
			if choice == 1:
				tag = node.attrib['CGOLD']
			else:
				#if node.attrib['CGOLD_YN'] == 'Not Applicable':
				#	return None
				tag = node.attrib['CGOLD_YN']
			CSubject = node[0].text.split()
			CBody =  node[1].text.split()
			#features['CSubject'] = tuple(node[0].text.split())
			#features['CBody'] = tuple(node[1].text.split())
			
			#count match words
			CSword_num = 0
			CBword_num = 0
			for CS_word in CSubject:
				if count_match_dict(CS_word,QSubject) == 1:
					CSword_num = CSword_num + 1
					try:
						#features['CSword(%s)' % CS_word] = features['CSword(%s)' % CS_word] + 1
						features['CSword(%s)' % CS_word] = 1
					except:
						pass
			for CB_word in CBody:
				if count_match_dict(CB_word,QBody) == 1:
					CBword_num = CBword_num + 1
					try:
						#features['CBword(%s)' % CB_word] = features['CBword(%s)' % CB_word] + 1
						features['CBword(%s)' % CB_word] = 1
					except:
						pass
				
			features['CSword_num'] = CSword_num
			features['CBword_num'] = CBword_num
			
			featureset.append([features,tag])
			features = {}
			features['QCATEGORY'] = data.attrib['QCATEGORY']
			
		return featureset
		#features['question'] = 
	for node_question in root:
		try:
			featureset = featureset + gender_features(node_question)
		except:
			pass
	print featureset[0:4]

	
	
	return featureset