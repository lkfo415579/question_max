
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
		features['QGOLD_YN'] = data.attrib['QGOLD_YN']
		#features['comments'] = []
		QSubject = data[0]
		features['QSubject'] = tuple(QSubject.text.split())
		QBody = data[1]
		features['QBody'] = tuple(QBody.text.split())
		
		del data[0]
		del data[0]
		for node in data:
			#print node
			tag = node.attrib['CGOLD']
			features['CSubject'] = tuple(node[0].text.split())
			features['CBody'] = tuple(node[1].text.split())
			featureset.append([features,tag])
		return featureset
		#features['question'] = 
	for node_question in root:
		featureset = featureset + gender_features(node_question)
		
	#print featureset[0]
	#print featureset[1]
	#print featureset[2]
	return featureset