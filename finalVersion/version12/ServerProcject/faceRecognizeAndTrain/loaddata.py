from torchvision.datasets import ImageFolder
from torchvision.transforms import Compose, ToTensor, Resize, RandomResizedCrop, RandomHorizontalFlip, Normalize
from torch.utils.data import random_split
from torch.utils.data import DataLoader 

def load_data(ds_path="./images", rate = 0.8, batch_size=200) :
    print("Enter LoadData")
    transform = Compose(
        [
            Resize((224, 224)), 
            # RandomHorizontalFlip(), 
            ToTensor(), 
            # Normalize(mean=(0.0, 0.0, 0.0), std=(1.0, 1.0, 1.0))
        ]
    )
    imgs_ds = ImageFolder(root=ds_path, transform=transform)
    print(imgs_ds.classes, imgs_ds.class_to_idx)
    total_len = len(imgs_ds)
    train_len = int(total_len * rate)
    train_ds, valid_ds = random_split(imgs_ds, [train_len, total_len - train_len])

    loader_train = DataLoader(dataset=train_ds, shuffle=True, batch_size=batch_size)
    loader_valid = DataLoader(dataset=valid_ds, shuffle=True, batch_size=batch_size)
    print("Return From LoadData")
    return  loader_train, loader_valid , imgs_ds.class_to_idx


# a, b = load_data()
# print(a, b)