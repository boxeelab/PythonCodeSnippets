

import argparse
parser = argparse.ArgumentParser()

parser.add_argument('--dir', type = str, default = 'pet_images/', help = 'Command line text parameter') 
parser.add_argument('--count', type = int, default = 2, help = 'Command line int paramter') 


argument =  parser.parse_args()
print(argument)

#try python command_line_argument.py --count 10
#try python command_line_argument.py --dir "test/"
#try python command_line_argument.py -h for help
