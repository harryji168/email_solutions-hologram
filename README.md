# Taipei 101 hologram

A 3D hologram page: a simplified Taipei 101 that looks like a solid miniature
sitting inside the phone. Tilt the phone to look around it, drag to turn it,
pinch to zoom.

- `index.html` - the page (three.js, off-axis projection driven by phone tilt)
- `taipei101.glb` - simplified Taipei 101 tower (508 m, eight flared modules)
- `build_taipei101.py` - generates the tower model (`pip install trimesh numpy scipy`)

Open the GitHub Pages address of this repository on a phone. On iPhone, tap
**Start hologram** and allow motion access.
