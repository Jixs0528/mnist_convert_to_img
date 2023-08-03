import os
from torchvision import datasets
from PIL import Image


train_loader = datasets.MNIST(root="data",train=True,download=True)
for i in range(10):
    if not os.path.exists("./data/images/trains/{}".format(i)):
        os.makedirs("./data/images/trains/{}".format(i))
index = [0] * 10
for digit, label in train_loader:
    digit.save("./data/images/trains/{}/{}_{}.jpg".format(label, label, index[label]))
    index[label] += 1
