
## What Are These Formats?






## PBM (Portable Bit Map)

A monochrome file format that uses ASCII 0's (white) and 1's (black).

```
P1
# hehe.pbm
24 7
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 1 0 0 1 0 0 1 1 1 1 0 0 1 0 0 1 0 0 1 1 1 1 0
0 1 0 0 1 0 0 1 0 0 0 0 0 1 0 0 1 0 0 1 0 0 0 0
0 1 1 1 1 0 0 1 1 1 0 0 0 1 1 1 1 0 0 1 1 1 0 0
0 1 0 0 1 0 0 1 0 0 0 0 0 1 0 0 1 0 0 1 0 0 0 0
0 1 0 0 1 0 0 1 1 1 1 0 0 1 0 0 1 0 0 1 1 1 1 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
```


## PGM (Portable Gray Map)

A grayscale format


```
P2
# hehe.pgm
24 7
255
0  0  0  0  0  0  0  0    0    0    0    0 0  0   0   0   0   0 0  0   0   0   0   0
0  63 0  0  63 0  0  126  126  126  126  0 0  189 0   0   189 0 0  254 254 254 254 0
0  63 0  0  63 0  0  126  0    0    0    0 0  189 0   0   189 0 0  254 0   0   0   0
0  63 63 63 63 0  0  126  126  126  0    0 0  189 189 189 189 0 0  254 254 254 0   0
0  63 0  0  63 0  0  126  0    0    0    0 0  189 0   0   189 0 0  254 0   0   0   0
0  63 0  0  63 0  0  126  126  126  126  0 0  189 0   0   189 0 0  254 254 254 254 0
0  0  0  0  0  0  0  0    0    0    0    0 0  0   0   0   0   0 0  0   0   0   0   0
```

## PPM (Portable Pixel Map)



```
P3
# feep.ppm
4 4
15
 0  0  0    0  0  0    0  0  0   15  0 15
 0  0  0    0 15  7    0  0  0    0  0  0
 0  0  0    0  0  0    0 15  7    0  0  0
15  0 15    0  0  0    0  0  0    0  0  0
```

## Magic Numbers

| Number | Format | Description | MIME Type |
|--------|--------|-------------|-----------|
| P1 | [Plain PBM](https://netpbm.sourceforge.net/doc/pbm.html#plainpbm) | Accepts 0 or 1 as pixel values and no line should be longer than 70 characters| `image/x-portable-bitmap`|
| P2 | [Plain PGM](https://netpbm.sourceforge.net/doc/pgm.html#plainpgm) | ... | `image/x-portable-graymap` |
| P3 | [Plain PPM](https://netpbm.sourceforge.net/doc/ppm.html#plainppm) |   | `image/x-portable-pixmap`|

| P4 | [Minimal PBM](https://netpbm.sourceforge.net/doc/pbm.html#minimal) |  ... | `image/x-portable-bitmap` |
| P5 | [Minimal PGM](https://netpbm.sourceforge.net/doc/pgm.html#minimal) | Maxval as 255 and goes from 0-255 | `image/x-portable-graymap`|
| P6 | [Minimal PPM](https://netpbm.sourceforge.net/doc/ppm.html#minimal) | Tripplets of RGB values (max 255 per value) | `image/x-portable-pixmap`|

Any format named "plain" is just ascii, whereas the minimal versions are primarily binary formats.


## References

- https://netpbm.sourceforge.net/doc/index.html#formats
    - [PGM Format Specification](https://netpbm.sourceforge.net/doc/pgm.html)
    - [PBM Format Specification](https://netpbm.sourceforge.net/doc/pbm.html)
    - [PPM Format Specification](https://netpbm.sourceforge.net/doc/ppm.html)
- [File Viewer](https://omnifile.co/view/)
