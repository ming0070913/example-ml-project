import torch
import torch.nn.functional as F
import torch.nn as nn


class Model(nn.Module):
    """
    An example pytorch model for classifying iris flower
    """

    def __init__(self, input_dim=4):
        super(Model, self).__init__()
        self.layer1 = nn.Linear(input_dim, 50)
        self.layer2 = nn.Linear(50, 50)
        self.layer3 = nn.Linear(50, 3)

    def forward(self, x):
        x = F.relu(self.layer1(x))
        x = F.relu(self.layer2(x))
        x = F.softmax(self.layer3(x), dim=1)
        return x
