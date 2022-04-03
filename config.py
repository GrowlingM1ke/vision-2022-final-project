# import the necessary packages
import torch
import os
# base path of the dataset
DATASET_PATH = os.path.join("data_lungs")
# define the path to the images and masks dataset
IMAGE_DATASET_PATH = os.path.join(DATASET_PATH, "image")
MASK_DATASET_PATH = os.path.join(DATASET_PATH, "label")
#define the path of only images containing haemorraghing
IMAGE_HAEM_DATASET_PATH = os.path.join("data_only_haem", "image")
MASK_HAEM_DATASET_PATH = os.path.join("data_only_haem", "label")
#define the path of only images containing haemorraghing
IMAGE_HAEM_4_DATASET_PATH = os.path.join("data_only_haem_4", "image")
MASK_HAEM_4_DATASET_PATH = os.path.join("data_only_haem_4", "label")
# define the test split
TEST_SPLIT = 0.15
# determine the device to be used for training and evaluation
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
# determine if we will be pinning memory during data loading
PIN_MEMORY = True if DEVICE == "cuda" else False

# define the number of channels in the input, number of classes,
# and number of levels in the U-Net model
NUM_CHANNELS = 1
NUM_CLASSES = 1
NUM_LEVELS = 3
# initialize learning rate, number of epochs to train for, and the
# batch size
INIT_LR = 0.001
NUM_EPOCHS = 50
BATCH_SIZE = 1
# define the input image dimensions
INPUT_IMAGE_WIDTH = 512
INPUT_IMAGE_HEIGHT = 512
# define threshold to filter weak predictions
THRESHOLD = 0.5
# define the path to the base output directory
BASE_OUTPUT = "output"
# define the path to the output serialized model, model training
# plot, and testing image paths
MODEL_PATH = os.path.join(BASE_OUTPUT, "unet_tgs_salt.pth")
PLOT_PATH = os.path.sep.join([BASE_OUTPUT, "plot.png"])
TEST_PATHS = os.path.sep.join([BASE_OUTPUT, "test_paths.txt"])