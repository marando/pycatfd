import dlib
import os
from TrainingDataUtil import TrainingDataUtil


class Trainer:
    DATA_DIR = 'data'
    DETECTOR_SVM = os.path.join(DATA_DIR, 'detector.svm')
    PREDICTOR_DAT = os.path.join(DATA_DIR, 'predictor.dat')

    def __init__(self, folder=TrainingDataUtil.training_data_dir, cpu_cores=8):
        self.__folder = folder
        self.__cpu_cores = cpu_cores
        self.__xml = '{0}/training.xml'.format(folder)

    def train_object_detector(self):
        self.__print_training_message('object detector')
        opt = dlib.simple_object_detector_training_options()
        opt.add_left_right_image_flips = True
        opt.C = 5
        opt.num_threads = self.__cpu_cores
        opt.be_verbose = True
        dlib.train_simple_object_detector(self.__xml, self.DETECTOR_SVM, opt)

    def train_shape_predictor(self):
        self.__print_training_message('shape predictor')
        opt = dlib.shape_predictor_training_options()
        opt.oversampling_amount = 300
        opt.nu = 0.05
        opt.tree_depth = 2
        opt.be_verbose = True
        opt.num_threads = self.__cpu_cores
        dlib.train_shape_predictor(self.__xml, self.PREDICTOR_DAT, opt)

    def __print_training_message(self, trainer):
        print 'Training {0} with {1} CPU codes.'.format(trainer,
                                                        self.__cpu_cores)
