# Taipei 101 hologram

A 3D hologram page: a simplified Taipei 101 that looks like a solid miniature
sitting inside the phone. Tilt the phone to look around it, drag to turn it,
pinch to zoom.

- `index.html` - the page (three.js, off-axis projection driven by phone tilt)
- `taipei101.glb` - simplified Taipei 101 tower (508 m, eight flared modules)
- `build_taipei101.py` - generates the tower model (`pip install trimesh numpy scipy`)

Open the GitHub Pages address of this repository on a phone. On iPhone, tap
**Start hologram** and allow motion access.

## Pyramid viewer mode

Tap **Pyramid viewer** (or open the page with `#pyramid` at the end of the
address) to show four side views of the spinning tower around the centre of
the screen, for a plastic hologram pyramid placed small end down on the phone.

## Sheet viewer mode

Tap the mode button twice (or open the page with `#sheet` at the end of the
address) to show one large tower for a single clear sheet leaning at 45
degrees over the screen. The sheet's bottom edge sits on the far side of the
phone and its top edge leans toward the viewer.

## Big screen mode

Open the page with `#screen` at the end of the address (or tap the mode button
until it shows) for one upright tower on black, for a projector or TV.

## Hand gestures

Tap **Hand gestures** and allow camera access. Move an open hand left or right
to turn the tower; pinch thumb and index finger and move up or down to zoom.
Works in every mode. Hand tracking uses MediaPipe and runs in the browser; no
video leaves the device.

## Videos for LED hologram fans

- `fan/taipei101_fan_720.mp4` - 720x720, for a large fan
- `fan/taipei101_smallfan_320.mp4` - 320x320, bolder and brighter, for a small 160-LED fan

Both are 10 seconds at 30 fps on a pure black background and loop cleanly.
