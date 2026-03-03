import sys
from PIL import Image

# Allowed GBC palette for Unown normal.gbcpal:
#	[$41ef, $20e7, $0000]
ALLOWED = [0x41EF, 0x20E7, 0x0000]

def gbc15_to_rgb888(v):
	# GBC uses 5 bits per channel (0..31). $7fff is (31,31,31).
	r5 = (v >> 0) & 0x1F
	g5 = (v >> 5) & 0x1F
	b5 = (v >> 10) & 0x1F
	# Expand 5-bit to 8-bit
	r8 = (r5 << 3) | (r5 >> 2)
	g8 = (g5 << 3) | (g5 >> 2)
	b8 = (b5 << 3) | (b5 >> 2)
	return (r8, g8, b8)

ALLOWED_RGB = [gbc15_to_rgb888(v) for v in ALLOWED]

def nearest_allowed(r, g, b):
	best_i = 0
	best_d = None
	for i, (ar, ag, ab) in enumerate(ALLOWED_RGB):
		dr = r - ar
		dg = g - ag
		db = b - ab
		d = dr*dr + dg*dg + db*db
		if best_d is None or d < best_d:
			best_d = d
			best_i = i
	return ALLOWED_RGB[best_i]

def main():
	if len(sys.argv) != 2:
		print("Usage: python force_unown_palette.py <path-to-png>")
		sys.exit(1)

	path = sys.argv[1]

	im = Image.open(path).convert("RGBA")
	pix = im.load()
	w, h = im.size

	changed = 0
	for y in range(h):
		for x in range(w):
			r, g, b, a = pix[x, y]
			if a == 0:
				continue
			nr, ng, nb = nearest_allowed(r, g, b)
			if (r, g, b) != (nr, ng, nb):
				pix[x, y] = (nr, ng, nb, a)
				changed += 1

	im.save(path)
	print(f"OK: {path} | pixels changed: {changed}")

if __name__ == "__main__":
	main()