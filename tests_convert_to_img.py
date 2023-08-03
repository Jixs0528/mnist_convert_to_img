import os
from torchvision import datasets
from PIL import Image


test_loader = datasets.MNIST(root="data",train=False,download=True)
for i in range(10):
    if not os.path.exists("./data/images/tests/{}".format(i)):
        os.makedirs("./data/images/tests/{}".format(i))
index = [0] * 10
for digit, label in test_loader:
    digit.save("./data/images/tests/{}/{}_{}.jpg".format(label, label, index[label]))
    index[label] += 1
