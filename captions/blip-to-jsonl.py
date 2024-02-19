import argparse
import os
import json
import glob
from pathlib import Path

#https://docs.aws.amazon.com/bedrock/latest/userguide/cm-titan-image.html
def main(args):
    #List all images in the directory
    dir_path = Path(args.captions_dir)
    output_file = Path(args.output_file)

    #Clear file if exists
    if output_file.exists():
        with open(output_file, 'w') as f:
            pass

    exts = args.image_extensions.split(",")
    files = [f for ext in exts for f in glob.glob(os.path.join(dir_path, '*.'+ext))]
    i = 0

    for file in files:
        with open(file, "r", encoding="utf-8") as f:

            name = Path(file).name
            file_name_parts = [name[:name.rfind(".")], name[name.rfind("."):]]

            caption_file = Path(args.captions_dir) / (file_name_parts[0] + "." + args.caption_extension)
            with open(caption_file, "r", encoding="utf-8") as f2:
                item = {
                    "image-ref": f"{args.ref_prefix}{file_name_parts[0] + file_name_parts[1]}",
                    "caption": f2.read()
                }

                with open(output_file, 'a') as f:
                    f.write(json.dumps(item) + "\n")

            i += 1

    print(f"Total files processed: {i}")


def setup_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    parser.add_argument("captions_dir", type=str, help="Directory containing captions")
    parser.add_argument("output_file", type=str, help="JSONL output file containing captions")
    parser.add_argument(
        "--image_extensions",
        type=str,
        default="jpg,jpeg,png,webp",
        help="Extension of image files",
    )
    parser.add_argument(
        "--caption_extension",
        type=str,
        default="txt",
        help="Extension of caption files",
    )
    parser.add_argument(
        "--ref_prefix",
        type=str,
        default="",
        help="Prefix to use in the image-ref tags",
    )

    return parser


if __name__ == "__main__":
    parser = setup_parser()
    args = parser.parse_args()

    main(args)
