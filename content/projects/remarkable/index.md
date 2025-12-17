---
title: "Remarkable File Sync Tool"
date: 2025-05-16
summary: Simple script and obsidian plugin to allow automaticlly importing screenshots into you documents and a script for bult exporting to pdf you remarkable files.
--- 

This script allows you to download files from your reMarkable tablet's file system, manage version control, and organize files efficiently.

## Prerequisites

- Python 3.x
- Required Python libraries: `requests`, `argparse`, `logging`
- reMarkable tablet connected to your network (default base URL: `http://10.11.99.1`)
- `jq` installed for JSON parsing (for manual usage of `curl` commands)

## Installation

1. Move the script to `/usr/local/bin/` and rename it to `rmsync` for convenient use:

```bash
   sudo mv sync.py /usr/local/bin/rmsync
```

## How to get the root file names

``` bash
curl --silent http://10.11.99.1/documents/ | jq -r '.[] | .VissibleName'
```

## get the names of the files in school folder

```bash
curl --silent http://10.11.99.1/documents/ea52b7cb-5b40-4fe6-803d-9bb363b00391 | jq -r '.[] | .VissibleName'
```

## downloading the pdf of a document

```bash
curl -OJL "http://10.11.99.1/download/a2bc2ef2-1f2b-48d6-93f4-65018d97aed7/10.1"
```

command to download every file from a folder

```bash
python3 sync.py "travel"
```


## Remarkable Frame Buffer 

The remarkable stores its frame buffer aka the screen in /dev/fb0  you can I copy  this over scp but this will need to be converted to a format lie png

### Remarkable image format 
The remarkable 1 has a resolution of 1872 x 1404 pixels
you can run 'fbset' sshed into your tablet you will get something like this 
```
mode "1404x1872-47" # D: 160.000 MHz, H: 88.594 kHz, V: 46.900 Hz geometry 1404 1872 1408 3840 16 timings 6250 32 326 4 12 44 1 accel false rgba 5/11,6/5,5/0,0/0 endmode
```
 the geometry line explains the odd resolution of the tablet  because yes it is 1872 x 1404 but they actually store more in the framebuffer than one screen.
 - **Visible width** = 1404
- **Visible height** = 1872
- **Stride** (virtual width) = 1408
- **Virtual height** = 3840
- **Bits per pixel** = 16

1.  Get the framebuffer.
```bash
ssh root@10.11.99.1 "cat /dev/fb0" > fb0dump
```
2.  trim the dump to only the visible screen.
```bash
head -c 5271552 fb0dump > fb0dump_visible
```
3. Use imageMagick to convert the dump to a png
```bash 
convert -size 1408x1872 -depth 16 gray:fb0dump_visible screenshot_uncropped.png

```
4. crop 4 columns off of unsued 
```bash 
convert screenshot_uncropped.png -crop 1404x1872+0+0 +repage screenshot.png
```
   