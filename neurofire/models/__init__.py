from .cantor.cantor import Cantor
from .unet.unet_2d import UNet2D
from .unet.unet_2p5d import UNet2p5D
from .unet.unet_3d import UNet3D


def get_model(name):
    assert name in globals(), "Model not found."
    return globals().get(name)
