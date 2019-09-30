import argparse
import io
import json
import pandas as pd
import pathlib
import sys
from google.cloud import vision
from google.protobuf import json_format

client = vision.ImageAnnotatorClient()


def ocr_image(path):
    path = pathlib.Path(path)
    image_content = path.read_bytes()
    gc_image = vision.types.Image(content=image_content)
    res = client.text_detection(image=gc_image)
    return res


def main(argv=None):
    if argv is None:
        argv = sys.argv[1:]
    parser = argparse.ArgumentParser(
        description="Extract text from images using Google Cloud Vision API.\n"
        "Must export environment variable GOOGLE_APPLICATION_CREDENTIALS first, "
        "see https://cloud.google.com/docs/authentication/getting-started"
    )
    parser.add_argument(
        "images",
        type=pathlib.Path,
        nargs="+",
        help="Path or multiple paths to images for OCR",
    )
    parser.add_argument(
        "output",
        type=pathlib.Path,
        help="Path to output file in which extracted texts from all images will be written",
    )
    args = parser.parse_args(argv)
    img_not_found = [not p.exists() for p in args.images]
    img_names = [p.stem for p in args.images]
    if any(img_not_found):
        raise ValueError("Images not found:", "\n".join(img_not_found))
    res = [ocr_image(p) for p in args.images]
    res_dict = {n: json_format.MessageToDict(r) for n, r in zip(img_names, res)}
    with args.output.with_suffix(".json").open("w") as f:
        json.dump(res_dict, f)
    texts = [
        r.full_text_annotation.text.encode("unicode_escape").decode("utf-8")
        for r in res
    ]
    out_df = pd.DataFrame(dict(name=img_names, text=texts))
    out_df.to_csv(args.output.with_suffix(".csv"), index=False)


if __name__ == "__main__":
    main()
