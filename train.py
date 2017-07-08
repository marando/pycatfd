import argparse
import multiprocessing
import os
from lib.Trainer import Trainer
from lib.TrainingDataUtil import TrainingDataUtil


def main():
    formatter = lambda prog: argparse.HelpFormatter(prog,
                                                    max_help_position=33)
    desc = '''
    Handles the training of the FHOG detector and facial landmark shape 
    predictor
    '''
    parser = argparse.ArgumentParser(description=desc,
                                     formatter_class=formatter)

    parser.add_argument('-t', '--train-all',
                        help='''
                        begin full training, which includes both FHOG detector 
                        and shape predictor training
                        ''',
                        action='store_true')

    parser.add_argument('-d', '--train-detector',
                        help='begin FHOG object detector training',
                        action='store_true')

    parser.add_argument('-p', '--train-predictor',
                        help='''
                        begin facial landmark shape predictor training 
                        ''',
                        action='store_true')

    parser.add_argument('-c', '--cpu-cores',
                        help='''
                        number of CPU cores to train with 
                        ''',
                        default=multiprocessing.cpu_count(),
                        metavar='<int>')

    parser.add_argument('-u', '--source-url',
                        help='download training data from url',
                        metavar='<url>')

    parser.add_argument('-a', '--archive',
                        help='''
                        compress current training data directory to tar gzip 
                        archive
                        ''',
                        action='store_true')

    parser.add_argument('-i', '--imglab',
                        help='''
                        Open imglab session for current training data
                        ''',
                        action='store_true')

    args = vars(parser.parse_args())

    if args['source_url']:
        TrainingDataUtil.download_training_data(args['source_url'])

    if args['archive']:
        TrainingDataUtil.archive_training_data()

    if args['train_all']:
        train_detector(args['cpu_cores'])
        train_predictor(args['cpu_cores'])

    if args['train_detector']:
        train_detector(args['cpu_cores'])

    if args['train_predictor']:
        train_predictor(args['cpu_cores'])

    if args['imglab']:
        parts = (
            'left_eye',
            'right_eye',
            'nose',
            'left_of_left_ear',
            'right_of_left_ear',
            'left_of_right_ear',
            'right_of_right_ear',
            'chin'
        )
        cmd = 'imglab {}/{} --parts "{}"'.format(
            TrainingDataUtil.training_data_dir,
            TrainingDataUtil.training_data_xml,
            ' '.join(parts)
        )
        os.system(cmd)


def train_detector(cpu_cores):
    TrainingDataUtil.extract_training_data()
    t = Trainer(TrainingDataUtil.training_data_dir, cpu_cores)
    t.train_object_detector()


def train_predictor(cpu_cores):
    TrainingDataUtil.extract_training_data()
    t = Trainer(TrainingDataUtil.training_data_dir, cpu_cores)
    t.train_shape_predictor()


main()
