import argparse
from scripts.train import train_model
from scripts.test import test_model

def main():
    parser = argparse.ArgumentParser(description="Image Deblurring with Deep Learning")
    parser.add_argument("--mode", type=str, required=True, choices=["train", "test"], help="Mode: train or test")
    parser.add_argument("--checkpoint", type=str, default=None, help="Path to model checkpoint for testing")
    args = parser.parse_args()

    if args.mode == "train":
        train_model()
    elif args.mode == "test":
        if not args.checkpoint:
            raise ValueError("Checkpoint path must be provided in test mode")
        test_model(args.checkpoint)

if __name__ == "__main__":
    main()
