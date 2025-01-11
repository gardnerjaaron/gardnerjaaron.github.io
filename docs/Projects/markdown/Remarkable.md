
# Remarkable File Sync Tool

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

command to download everything file from a folder

```bash
python3 sync.py "travel"
```

TODO

- upload
- allow updateing of file/ only download the ones that have changed
  - this is dont using git but needs to be poslihed some.
- make a small ui for download and upload this should be optional to use and the command line shoudl still be a option so that is can be automated
- work on some scripts to automate it on start up if there is a device detected
  - seems possible to automate but 
- add fuctionalty for folders within folders to be maintained and for them to stay in the correct order
- backup mode where it dowloads everything and compresses it for a more robust backup method

