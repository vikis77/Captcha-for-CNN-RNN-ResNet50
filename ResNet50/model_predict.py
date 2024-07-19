import torch
from torchvision import transforms
from buildCaptchaModel import CaptchaModel
import PIL
from PIL import Image
import os
from torch.utils.data import DataLoader, Dataset
# from CaptchaDataset import CaptchaDataset
import glob
def single_predict(model, image, decoding_dict, device="cpu"):

    img = transforms.Compose(
        [
            transforms.Resize((64, 192)),
            transforms.CenterCrop((64, 192)),
            transforms.Grayscale(num_output_channels=1),
            transforms.ToTensor(),
            transforms.Normalize((0.7570), (0.3110)),
        ]
    )(image)

    if img.dim() == 3:
        img = img.unsqueeze(0)
    model.to(device)
    model.eval()
    with torch.inference_mode():
        out = model(img.to(device))

    label = []
    encoded_vector = out.reshape(34, 4).argmax(0)
    for key in encoded_vector.detach().cpu().numpy():
        label.append(decoding_dict[key])
    return "".join(label)

