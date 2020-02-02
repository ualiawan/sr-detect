from os.path import join
from torchvision.transforms import Compose, ToTensor
from dataset import DatasetFromFolderEval

def transform():
    return Compose([
        ToTensor(),
    ])

def get_eval_set(lr_dir, upscale_factor):
    return DatasetFromFolderEval(lr_dir, upscale_factor,
                             transform=transform())

