import argparse
import qrcode
import image

parser = argparse.ArgumentParser()
parser.add_argument("-u", "--url", help = "URL input")

args = parser.parse_args()

if args.url:
	url=args.url
	img=qrcode.make(url)
	img.save("/home/ranjeet/Desktop/qr.jpg")
    