with open('./datasets/split_file/VID_val_file.txt', 'w') as f:
    lines = open('./datasets/split_file/VID_val_videos.txt').readlines()
    for line in lines:
        if line.startswith('val/ILSVRC2015_val_00008000'):
            break
        f.write(line)