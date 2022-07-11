import torch 
from torchvision import datasets
from torchvision.transforms import ToTensor


trainingData = datasets.CIFAR10(
    root = "./data/CIFAR10",
    train = True,
    download=True,
    transform = ToTensor()
)
testData = datasets.CIFAR10(
    root = "./data/CIFAR10",
    train = False,
    download=True,
    transform = ToTensor()
)