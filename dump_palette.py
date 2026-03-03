from pathlib import Path

def bgr15_to_rgb888(c):
    r = (c >> 0) & 0x1F
    g = (c >> 5) & 0x1F
    b = (c >> 10) & 0x1F
    return (r * 255 // 31, g * 255 // 31, b * 255 // 31)

p = Path(r"gfx/pokemon/pidgey/normal.gbcpal")
data = p.read_bytes()

print("Byte length:", len(data))

colors = []
for i in range(0, len(data), 2):
    val = int.from_bytes(data[i:i+2], "little") & 0x7FFF
    colors.append(val)

print("Raw 15-bit:", [hex(c) for c in colors])
print("RGB888:", [bgr15_to_rgb888(c) for c in colors])