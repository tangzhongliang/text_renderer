import os
from shutil import rmtree
from glob import glob
import argparse


def main(font_dir):
    zips = glob(font_dir + '/*.zip')
    tmp_dir = 'tmp_zip'
    if os.path.exists(tmp_dir):
        rmtree(tmp_dir)
    for zip_fp in zips:
        os.system(f'unzip {zip_fp} -d {tmp_dir}')
        font_fps = glob(tmp_dir + '/*/*', recursive=True)
        for font_fp in font_fps:
            if any(font_fp.lower().endswith(suffix) for suffix in ['ttf', 'ttc', 'otf']):
                os.system(f'mv {font_fp} {font_dir}')
                break
    if os.path.exists(tmp_dir):
        rmtree(tmp_dir)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_dir', type=str, default='./data/fonts/chn',
                        help='很多zip文件所在的路径')
    args = parser.parse_args()
    main(args.input_dir)
