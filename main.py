    
data_dir = ["ants_image", "ants_label","bees_image", "bees_label"]
for data_name in data_dir:
  data_label_idx = data_name.split("_")
  print(data_label_idx)