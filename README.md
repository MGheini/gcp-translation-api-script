# gcp-translation-api-script
A script to talk to Google Cloud Translation API and get your files Google-translated

First, follow Cloud Translation Quickstart [here](https://cloud.google.com/translate/docs/quickstart-client-libraries) to set up a GCP project, set the required environment variable, and install the client library. Then you can use this script per the description below:

```
usage: g_translate.py [-h] -i INPUT -s SOURCE [-t TARGET] [-o OUTPUT]

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        Input file path (default: None)
  -s SOURCE, --source SOURCE
                        Source language (default: None)
  -t TARGET, --target TARGET
                        Target language (default: en)
  -o OUTPUT, --output OUTPUT
                        Output file path (default: gt_out.txt)
```
