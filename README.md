# Patho IDs

Extract identifiers from histological slides using the [Google
Cloud Vision API](https://cloud.google.com/vision/docs/handwriting)
for optical character recognition.

## Installation

```bash
pip install git+https://github.com/clemenshug/patho-ids
```

In order to use this script a Google Cloud account is required, see
https://cloud.google.com/docs/authentication/getting-started for details.

## Usage Example

```bash
patho_ids image1.png image2.png output
```

Gives the following output in csv format:

```
name,text
image1,S14- 64142\n82
image2,S15- 72662\nA3
```
