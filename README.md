# Hologram sample

A sample 3D hologram page: a model that looks like a solid miniature sitting
inside the phone. Tilt the phone to look around it, drag to turn it, pinch to
zoom. A button switches between the two sample models.

- `index.html` - the page (three.js, off-axis projection driven by phone tilt)
- `taipei101.glb` - simplified Taipei 101 tower (508 m, eight flared modules)
- `apartment.glb` - made-up one-bedroom apartment
- `build_taipei101.py` - generates the tower model (`pip install trimesh numpy scipy`)

Open the GitHub Pages address of this repository on a phone. On iPhone, tap
**Start hologram** and allow motion access.
