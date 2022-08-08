## MC-Blur: A Comprehensive Benchmark for Image Deblurring
## Kaihao, Zhang and Tao, Wang and Wenhan,Luo and Boheng, Chen and Wenqi, Ren and Stenger, Bjorn and Wei, Liu and Hongdong, Li and Ming-Hsuan, Yang
## https://arxiv.org/abs/2112.00234

## Download MC-Blur for image deblurring

import os
import gdown
import shutil

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--data', type=list,
                    default=['RHM_250_Test', 'RHM_500_Test', 'RHM_1000_Test', 'RHM_250_500_1000_train_test',
                             'UHDM_train_test', 'LSD_train_test', 'RMBQ'])
args = parser.parse_args()

### Google drive IDs for MC-Blur dataset

## For RHM dataset
RHM_250_Test = '1hoCFNeP1GOszaJfLABBw35hCQQKWPMhV'  ## https://drive.google.com/file/d/1hoCFNeP1GOszaJfLABBw35hCQQKWPMhV

RHM_500_Test = '13payJmIY6mssFXMSuOwf1aosA3n6bXb6'  ## https://drive.google.com/file/d/13payJmIY6mssFXMSuOwf1aosA3n6bXb6

RHM_1000_Test = '1HJqV6Ogve-G6YGYJDH7MD5nKAQOTnVMG'  ## https://drive.google.com/file/d/1HJqV6Ogve-G6YGYJDH7MD5nKAQOTnVMG

RHM_250_500_1000_train_test = '1V9Ac0Bw9wdoo50y8JM0F4VVh1jNGTP6m '  ## https://drive.google.com/file/d/1V9Ac0Bw9wdoo50y8JM0F4VVh1jNGTP6m

## For UHDM

UHDM_train_test = '1qToTBej21VC7n49L_36FjmuQisjM3xPf'  ## https://drive.google.com/file/d/1qToTBej21VC7n49L_36FjmuQisjM3xPf

## For LSD

LSD_train_test = '19C56VIxChcvcCylKpAlK1pqYo16c0D_k'  ## https://drive.google.com/file/d/19C56VIxChcvcCylKpAlK1pqYo16c0D_k

## For RMBQ

RMBQ = '1ydAuaPy8uh_s3yk0G9raEYyC7z8BGvMl'  ## https://drive.google.com/file/d/1ydAuaPy8uh_s3yk0G9raEYyC7z8BGvMl

for data in args.data:
    if data == 'RHM_250_Test':
        print('RHM 250 fps Testing Data!')
        gdown.download(id=RHM_250_Test, output='Datasets/', quiet=False)
        print('Extracting RHM 250 fps Testing data...')
        shutil.unpack_archive('Datasets/motion_avg_250fps.zip', 'Datasets')
        os.remove('Datasets/motion_avg_250fps.zip')

    if data == 'RHM_500_Test':
        print('RHM 500 fps Testing Data!')
        gdown.download(id=RHM_500_Test, output='Datasets/', quiet=False)
        print('Extracting RHM 500 fps Testing data...')
        shutil.unpack_archive('Datasets/motion_avg_500fps.zip', 'Datasets')
        os.remove('Datasets/motion_avg_500fps.zip')

    if data == 'RHM_1000_Test':
        print('RHM 1000 fps Testing Data!')
        gdown.download(id=RHM_1000_Test, output='Datasets/', quiet=False)
        print('Extracting RHM 1000 fps Testing data...')
        shutil.unpack_archive('Datasets/motion_avg_1000fps.zip', 'Datasets')
        os.remove('Datasets/motion_avg_1000fps.zip')

    if data == 'RHM_250_500_1000_train_test':
        print('RHM_250_500_1000 training and Testing Data!')
        gdown.download(id=RHM_250_500_1000_train_test, output='Datasets/', quiet=False)
        print('Extracting RHM training and Testing data...')
        shutil.unpack_archive('Datasets/motion_avg.zip', 'Datasets')
        os.remove('Datasets/motion_avg.zip')

    if data == 'UHDM_train_test':
        print('UHDM training and Testing Data!')
        gdown.download(id=UHDM_train_test, output='Datasets/', quiet=False)
        print('Extracting UHDM training and Testing data...')
        shutil.unpack_archive('Datasets/Conv.zip', 'Datasets')
        os.remove('Datasets/Conv.zip')

    if data == 'LSD_train_test':
        print('LSD training and Testing Data!')
        gdown.download(id=LSD_train_test, output='Datasets/', quiet=False)
        print('Extracting LSD training and Testing data...')
        shutil.unpack_archive('Datasets/defocus_crop.zip', 'Datasets')
        os.remove('Datasets/defocus_crop.zip')

    if data == 'RMBQ':
        print('RMBQ Data!')
        gdown.download(id=LSD_train_test, output='Datasets/', quiet=False)
        print('Extracting RMBQ data...')
        shutil.unpack_archive('Datasets/real.zip', 'Datasets')
        os.remove('Datasets/real.zip')

print('Download completed successfully!')
