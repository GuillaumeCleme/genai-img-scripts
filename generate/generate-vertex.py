import argparse
import os
import json
import glob
from pathlib import Path
import requests
import time
import base64



def main(args):
    
    output_dir = Path(args.output_dir)
    
    #Send POST call to Vertex AI
    headers = {
        "Authorization": f"Bearer {args.token}",
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Charset": "UTF-8"
    }

    data = {
        "instances": [
            {
                "prompt": args.prompt
            }
        ],
        "parameters": {
            "sampleCount": args.sample_count
        }
    }

    response = requests.post(args.url, json=data, headers=headers)

    if(response.status_code == 200):
        json = response.json()
        
        for image in json["predictions"]:
            #Write the image to a file
            with open(os.path.join(output_dir,"image-" + str(time.time()) + ".png"), "wb") as f:
                f.write(base64.b64decode(image["bytesBase64Encoded"]))
    else:
        print(f"Error: {response.text}")


def setup_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    parser.add_argument("token", type=str, help="API Token for the Vertex Imagen service")
    parser.add_argument("output_dir", type=str, help="Directory to store the generated images")
    parser.add_argument("prompt", type=str, help="Prompt to use for the generation")
    parser.add_argument("--url", type=str, help="API endpoint for the Vertex Imagen service", default="https://us-central1-aiplatform.googleapis.com/v1/projects/genaitesting-410722/locations/us-central1/publishers/google/models/imagegeneration:predict")
    parser.add_argument(
        "--sample_count",
        type=int,
        default=2,
        help="Sample count for the generation",
    )

    return parser


if __name__ == "__main__":
    parser = setup_parser()
    args = parser.parse_args()

    main(args)