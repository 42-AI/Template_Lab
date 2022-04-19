import pytorch_lightning as pl
import torch
import torch.nn.functional as F
from torch import nn


class SimpleConvNet(nn.Module):
    def __init__(
        self,
        input_channel: int = 784,
        dropout: float = 0.25,
        n_classes: int = 10,
    ):
        super().__init__()
        self.conv_1 = nn.Conv2d(input_channel, 32, kernel_size=3, stride=1, padding=1)
        self.norm_1 = nn.BatchNorm2d(32)

        self.conv_2 = nn.Conv2d(32, 64, kernel_size=3, stride=1)
        self.norm_2 = nn.BatchNorm2d(64)

        self.pool = nn.MaxPool2d(2, 2)
        self.drop = nn.Dropout(p=dropout)

        self.fc_1 = nn.Linear(64 * 6 * 6, 512)
        self.fc_2 = nn.Linear(512, 128)
        self.fc_3 = nn.Linear(128, n_classes)

        self.softmax = nn.Softmax(dim=1)

    def forward(self, X: torch.Tensor) -> torch.Tensor:
        # CNN
        # Block 1
        X = self.conv_1(X)
        X = self.norm_1(X)
        X = self.drop(X)
        X = F.relu(self.pool(X))
        # Block 2
        X = self.conv_2(X)
        X = self.norm_2(X)
        X = self.drop(X)
        X = F.relu(self.pool(X))

        # Flatten
        X = torch.flatten(X, 1)

        # FCN
        # Layer 1
        X = self.drop(X)
        X = self.fc_1(X)
        X = F.relu(X)
        # Layer 2
        X = self.drop(X)
        X = self.fc_2(X)
        x = F.relu(X)
        X = self.drop(X)
        # Layer 3
        X = self.fc_3(X)

        # Softmax
        X = self.softmax(X)
        return X
