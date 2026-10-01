import torch
from torch.utils.data import Dataset
import os
from PIL import Image

class Mydata(Dataset):
  def __init__(self, root_dir, image_dir, label_dir):
    # **_image为数据, **_label为标签
    self.root_dir = root_dir
    self.image_dir = image_dir
    self.label_dir = label_dir
    self.data = os.listdir(os.path.join(root_dir, image_dir))
    self.label = os.listdir(os.path.join(root_dir, label_dir))
    
  def __getitem__(self, idx):
    with open(os.path.join(self.root_dir, self.label_dir, self.label[idx]), 'r') as f:
            label = f.readline()
    
    img = Image.open(os.path.join(self.root_dir, self.image_dir, self.data[idx]))
    return {'label': label, 'img': img}
  def __len__(self):
    return len(self.data)
root_dir = "datasets/ants-bees/train"
image_dir = "ants_image"
label_dir = "ants_label"
ants_data = Mydata(root_dir, image_dir, label_dir)
image_dir = "bees_image"
label_dir = "bees_label"
bees_data = Mydata(root_dir, image_dir, label_dir)
train_data = ants_data+bees_data
print(train_data[0])