import sys
from PIL import Image

image0 = Image.open(sys.argv[1])
image1 = Image.open(sys.argv[2])

w0, h0 = image0.size
w1, h1 = image1.size

assert(h0 == h1)

h = h0

merged = Image.new("RGBA", (w0+w1, h))
merged.paste(image0, ( 0, 0))
merged.paste(image1, (w0, 0))

merged.save("merged.png")

