import argparse
from main import start_bot

def parse_args():
    parser = argparse.ArgumentParser(description='Outreach automation bot')
    parser.add_argument('-d','--dev', help='Enables developer mode', action='store_true')
    parser.add_argument('-p','--prospect', help='Enables ChatGPT to write prospecting emails', action='store_true')
    parser.add_argument('-e','--email', help='Enables automatic sending of generated prospecting emails', action='store_true')
    
    
    args = vars(parser.parse_args())

    bType = input("Business type: ")
    location = input("Location: ")
    radius = input("Radius (metres): ")

    print(args)
    start_bot(bType, location, radius, dev=args['dev'], prospect=args['prospect'], email=args['email'])


if __name__ == "__main__":
    parse_args()
