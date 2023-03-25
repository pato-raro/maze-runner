'''from argparse import ArgumentParser, Namespace
parser = ArgumentParser()
parser.add_argument('a', help="Base", type=int)
parser.add_argument('b', help = "Exponent", type = int)
parser.add_argument("-v", help = "Verbose", action = 'count')
args: Namespace = parser.parse_args()
if args.v == 0:
    print(args.a ** args.b)
elif args.v == 1:
    print("Result is:", args.a ** args.b)
else:
    print("Oke")'''