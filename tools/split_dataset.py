import argparse
import os.path as osp
import random
train_scale = 0.9
def split_dataset(label):
    root = osp.dirname(label)
    train_label = osp.join(root, 'train.txt')
    test_label = osp.join(root, 'test.txt')
    with open(label,'r') as f:
        lines = f.readlines()
    train_f = open(train_label, 'w') 
    test_f = open(test_label, 'w') 
    for line in lines:
        if not len(line):
            continue
        proba = random.random()
        if proba < train_scale:
            train_f.write(line)
        else:
            test_f.write(line)
    train_f.close()
    test_f.close()
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='输入 labels.txt 标签数据，输出train.txt,test.txt')
    parser.add_argument('--label', type=str, default='')
    flags, _ = parser.parse_known_args()
    split_dataset(flags.label)
     

