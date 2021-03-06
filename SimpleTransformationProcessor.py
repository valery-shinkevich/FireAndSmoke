from ImageProcessor import ImageProcessor

class SimpleTransformationProcessor(ImageProcessor):
	def __init__(self, transformation):
		self.transformation = transformation

	def process(self, manager):
		#print manager.get('swir', 0)
		img = manager.get('rgb', 0)
		res = self.transformation.transform(img)
		return (img, res)