import argparse
import os
import glob
from pathlib import Path
import csv

def main(args):
    #List all images in the directory
    captions_file = Path(args.captions_file)
    captions_ext = args.captions_extension
    output_dir = Path(args.output_dir)
    i = 0

    with open(captions_file, 'r') as csv_file:

        csv_reader = csv.reader(csv_file)
        csv_reader.__next__() # skip header

        for row in csv_reader:
            file_name = row[0]
            caption = row[1]

            file_name = file_name[:file_name.rfind(".")]

            with open(output_dir / (file_name + "." + captions_ext), "w", encoding="utf-8") as caption_file:
                caption_file.write(caption)
                i += 1
        
    print(f"Total files processed: {i}")


def setup_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    parser.add_argument("captions_file", type=str, help="CSV file containing captions")
    parser.add_argument("output_dir", type=str, help="Output directory where caption files should be written")
    parser.add_argument(
        "--captions_extension",
        type=str,
        default="txt",
        help="Extension of caption files",
    )

    return parser


if __name__ == "__main__":
    parser = setup_parser()
    args = parser.parse_args()

    main(args)
