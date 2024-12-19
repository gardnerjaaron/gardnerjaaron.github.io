## To make it a script move to /usr/local/bin/ and remae to rmsync

## How to get the root file names
```
curl --silent http://10.11.99.1/documents/ | jq -r '.[] | .VissibleName'
```



## get the names of the files in school folder 
```
curl --silent http://10.11.99.1/documents/ea52b7cb-5b40-4fe6-803d-9bb363b00391 | jq -r '.[] | .VissibleName'
```


## downloading the pdf of a document 
```
curl -OJL "http://10.11.99.1/download/a2bc2ef2-1f2b-48d6-93f4-65018d97aed7/10.1"
```


command to download everything file from a folder 
```
python3 sync.py "travel"
```


TODO 
- specify a plce to put the files once they are downloaded 
- recursive into folders beyond root / folders in folders 
- upload 
- fix error with some random files 
- allow updateing of file/ only download the ones that have changed 
- make a small ui for download and upload this should be optional to use and the command line shoudl still be a option so that is can be automated 
- work on some scripts to automate it on start up if there is a device detected 
- add fuctionalty for folders within folders to be maintained and for them to stay in the correct order
- backup mode where it dowloads everything and compresses it for a more robust backup method 
- 
