# xfbin_rebuilder
# .xfbin Rebuilder

## Overview
This script is specifically designed to fix `.xfbin` files extracted using **VGMToolbox** from `.cpk` archives. Possibly due to extraction quirks, the resulting `.xfbin` files may retain `.cpk` headers, requiring a second extraction into `.bin` segments. This tool reconstructs proper `.xfbin` files from those `.bin` segments.

## How to Use

### Preparation:
1. Extract your `.cpk` archive using **VGMToolbox** `(Misc. Tools > Extraction Tools > Common Archives > CRI CPK Archive Extractor)`.
2. Perform a second .cpk extraction on the resulting `.xfbin` files to generate `.bin` segments within a folder labeled as:

```plaintext
VGMT_CPK_EXTRACT_<original_filename>.xfbin
```

### Running the Script:
1. Place `xfbin_rebuilder.py` into the parent directory containing your extracted folders.
2. Run the script:

```bash
python xfbin_rebuilder.py
```

The script will automatically:
- Identify relevant folders.
- Assemble the `.bin` segments into valid `.xfbin` files.
- Remove the temporary extraction folders once completed.

## Dependencies
- Python 3.x (no additional libraries required)

## License
MIT License

