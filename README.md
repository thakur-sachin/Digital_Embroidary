# Digital Embroidery

Embroidery designs generated from code. The scripts write Janome `.jef` files byte by byte, so a shape defined mathematically can be stitched directly on an embroidery machine.

| File | What it does |
|---|---|
| `main.py` | Writes `square5.jef`: a 1 cm square stitched in 1 mm steps, with every header field of the JEF format annotated |
| `heart.py` | Fills the implicit heart curve `(x² + y² − 1)³ − x²y³ ≤ 0` with stitch points and writes it as a JEF file |

## Usage

```bash
pip install numpy
python main.py    # writes square5.jef
python heart.py   # writes the heart design
```

Load the generated `.jef` onto a JEF-compatible machine, or preview it in any embroidery viewer.

## How the format works

A JEF file is a fixed header (stitch offset, date, thread count, stitch count, hoop size, boundaries, thread colors) followed by stitches stored as signed 8-bit relative moves `(dx, dy)` in 0.1 mm units. Control codes begin with `128`: `128, 2` starts a jump and `128, 16` marks the last stitch.

## License

See [LICENSE](LICENSE).
