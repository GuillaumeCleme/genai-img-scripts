import argparse
import os
import glob
from pathlib import Path
import csv

def main(args):
    #List all images in the directory
    dir_path = Path(args.captions_dir)
    output_file = Path(args.output_file)

    #Clear file if exists
    if output_file.exists():
        with open(output_file, 'w') as f:
            pass

    captions_exts = args.captions_extentions.split(",")
    images_exts = args.image_extentions.split(",")

    images = [f for ext in images_exts for f in glob.glob(os.path.join(dir_path, '*.'+ext))]
    i = 0

    with open(output_file, 'w', newline='') as csv_file:

        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(["file", *captions_exts])

        for image in images:
            data = []
            image_name = Path(image).name
            data.append(image_name)

            for ext in captions_exts:
                caption_file = dir_path / (image_name[:image_name.rfind(".")]+"."+ext)
                if caption_file.exists():
                    with open(caption_file, "r", encoding="utf-8") as f:
                        data.append(f.read().strip())
                        i += 1
                else:
                    data.append("")

            csv_writer.writerow(data)

    print(f"Total files processed: {i}")


def setup_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    parser.add_argument("captions_dir", type=str, help="Directory containing captions")
    parser.add_argument("output_file", type=str, help="CSV output file containing captions")
    parser.add_argument(
        "--image_extentions",
        type=str,
        default="jpg,jpeg,png,webp",
        help="Extension of image files",
    )
    parser.add_argument(
        "--captions_extentions",
        type=str,
        default="txt",
        help="Extension of caption files",
    )

    return parser


if __name__ == "__main__":
    parser = setup_parser()
    args = parser.parse_args()

    main(args)
