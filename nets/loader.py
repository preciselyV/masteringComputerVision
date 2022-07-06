import torch 
from torchvision import datasets
from torchvision.transforms import ToTensor


trainingData = datasets.FashionMNIST(
    root = "./data",
    train = True,
    download=True,
    transform = ToTensor()
)
trainingData = datasets.FashionMNIST(
    root = "./data",
    train = True,
    download=True,
    transform = ToTensor()
)