import dlib
from DetectorResult import DetectorResult
from lib.Trainer import DETECTOR_SVM
from lib.Trainer import PREDICTOR_DAT
from skimage import io


class Detector:
    def __init__(self, input_image):
        self.input_image = input_image
        self.image_data = io.imread(input_image)
        self.detector = dlib.fhog_object_detector(DETECTOR_SVM)
        self.predictor = dlib.shape_predictor(PREDICTOR_DAT)
        self.result = DetectorResult()

    def detect(self):
        self.result.faces = self.detector(self.image_data, 1)
        self.result.face_count = len(self.result.faces)
