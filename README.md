# 16bit2rgb
A python script for 16 bit TIFF to 24bit RGB PNG conversion

Accepting 16 bit .tiff files (ex. [the FLIR thermal dataset](https://www.flir.com/oem/adas/adas-dataset-form/)), the script outputs 24 bit RGB .png files.

## Usage
```
python 16bit2rgb.py INPUT_FILE_PATH --out OUTPUT_DIR
```
`INPUT_FILE_PATH` can be represented using a wild card (ex. `'/img/*.tiff'`).
You can use the following options:
- `--out` specify the output location (default: current directory)
- `--map` specify the colour map named by matplotlib (default: `CMRmap`)
- `--min_val` specify the minimum pixel value
- `--max_val` specify the maximum pixel value

If you specify both `--min_val` and `--max_val`, it skips to find those values. Otherwise, it tries to find those values in the specified files.
