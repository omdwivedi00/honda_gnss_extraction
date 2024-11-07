# coding: utf8
import os
import argparse
import configparser
import glob
import subprocess

parser = argparse.ArgumentParser(description='gnss parser refarence system')
parser.add_argument('--src', metavar='DIR', help='path to data directory.')
parser.add_argument('--dst', metavar='DIR', help='path to output directory.')
parser.add_argument('--config', default='./gnss_config/gnss_parser.ini' , help='path to config file.')


def make_dir(dir):
    """make directory
    Args:
        dir(str): directory path
    """
    if not os.path.isdir(dir):
        os.umask(0)
        os.makedirs(dir, mode=0o777)


def main():
  args = parser.parse_args()
  src_dir = args.src
  dst_dir = args.dst
  config_path = args.config

  config_ini = configparser.ConfigParser()
  config_ini.read(config_path)

  gnss_parser = config_ini['EXE']['gnss_parser']

  l_gnss_bin = glob.glob(os.path.join(src_dir, "*.bin"))
  for gnss_bin in l_gnss_bin:
     print("bin:{}".format(gnss_bin))
    #  binname = os.path.splitext(os.path.basename(gnss_bin))[0]
    #  save_dir = os.path.join(dst_dir, binname)
    #  make_dir(save_dir)
    #  subprocess.call([gnss_parser, '-i', gnss_bin, '-o', save_dir])
     make_dir(dst_dir)
     subprocess.call([gnss_parser, '-i', gnss_bin, '-o', dst_dir])

if __name__ == '__main__':
    main()
