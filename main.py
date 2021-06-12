from glob import glob
from tqdm import tqdm
import cv2

filenames = glob(r'C:\Users\Alcatraz\Downloads\archive\img_align_celeba\img_align_celeba\*')

if __name__ == '__main__':
    # __name__    for filename in tqdm(filenames, total=len(filenames)):
    #         print(cv2.imread(filename).shape)
    print(cv2.imread(filenames[0]))
