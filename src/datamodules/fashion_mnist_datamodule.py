from src.datamodules.mnist_datamodule import MNISTDataModule
from torchvision.datasets import FashionMNIST


class FashionMNISTDataModule(MNISTDataModule):

    def prepare_data(self):
        """Download data if needed.
        This method is called only from a single GPU.
        Do not use it to assign state (self.x = y).
        """
        FashionMNIST(self.hparams.data_dir, train=True, download=True)
        FashionMNIST(self.hparams.data_dir, train=False, download=True)
