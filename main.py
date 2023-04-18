from PIL import Image
from PIL.PngImagePlugin import PngImageFile
from typing import Tuple

def parse_num(num: int) -> str:
	num: str = str(num)
	new_str: str = ''
	digit_num: int = 0
	for index in range(len(num) - 1, -1, -1):
		if not digit_num % 3:
			new_str = ' ' + new_str
			digit_num = 0
		digit_num += 1
		new_str = num[index] + new_str
	return new_str.strip(' ')


def RGB_to_hex(clr: Tuple[int, int, int]) -> str:
	hexColor: str = ''
	for i in clr:
		a = str(hex(i))[2:]
		if a == '0':
			hexColor += a
		hexColor += a
	return '#' + hexColor.upper()


def avg_color(image: PngImageFile) -> None:
	redSum: int = 0
	greenSum: int = 0
	blueSum: int = 0
	numPixels: int = 0

	for i in image.getdata():
		numPixels += 1
		redSum += i[0]
		greenSum += i[1]
		blueSum += i[2]

	avgColor: Tuple[int, int, int] = (int(redSum / numPixels), int(greenSum / numPixels), int(blueSum / numPixels))

	print('Number of pixels:', parse_num(numPixels))
	print('Sum of red:', parse_num(redSum))
	print('Sum of green:', parse_num(greenSum))
	print('Sum of blue:', parse_num(blueSum))
	print('Average color:', avgColor)
	print('Average color in hexadecimal:', RGB_to_hex(avgColor))



if __name__ == '__main__':
	print('Welcom to the Most Common Color program!')
	while True:
		path: str = input("Enter a path to the image: ")
		image: PngImageFile = Image.open(path)
		avg_color(image)
		print('\nDo you want to continue? (y/n) ', end=' ')
		if input().lower() != 'y':
			break
	print("Thank you! Bye!")
