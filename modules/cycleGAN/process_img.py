from torch.utils.data import DataLoader
import torchvision.transforms as transforms
from torchvision.datasets import ImageFolder

from CycleGan import cycle_gan
from img_proc import scale, save_image_tr

import sys
import os


transform_test = transforms.Compose([transforms.Resize(720),  # puedes cambiar el tamaño de resize
                                    transforms.ToTensor()])

print(os.getcwd())
image_path_test_x = './modules/cycleGAN/input_imgs/'
#image_path_test_x = './input_imgs/'

test_x = ImageFolder(image_path_test_x, transform_test)

test_loader_x = DataLoader(dataset=test_x, batch_size=1, shuffle=False)

model = cycle_gan(training=False, device='cuda')  # Si tienes gpu cambiar 'cpu' -> 'cuda'

Style = 'cyberpunk/'

if len(sys.argv) > 1:
    Style = sys.argv[1]+'/'

dir_weights = './modules/cycleGAN/model_weights/' + Style
#dir_weights = './model_weights/' + Style


print(dir_weights)

# pesos disponibles para probar 84, 100, 256
model.load_weights(dir_weights,256)

for num, batch in enumerate(test_loader_x):
    img, _ = batch
    model.set_input_A(scale(batch[0]))
    model.forward_AB()

    save_image_tr(model.fake_B, num, 0, './modules/cycleGAN/samples', 'B')
