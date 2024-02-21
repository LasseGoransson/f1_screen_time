import cv2
import os
import argparse
from tqdm import tqdm

def extract_frames(video_path, output_folder, frame_rate):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    video_capture = cv2.VideoCapture(video_path)
    frame_count = 0

    total_frames = int(video_capture.get(cv2.CAP_PROP_FRAME_COUNT))
    with tqdm(total=total_frames, desc="Extracting frames", unit="frame") as pbar:
        while True:
            success, frame = video_capture.read()
            if not success:
                break

            if frame_count % frame_rate == 0:
                frame_name = f"frame_{frame_count // frame_rate}.jpg"
                frame_path = os.path.join(output_folder, frame_name)
                cv2.imwrite(frame_path, frame)

            frame_count += 1
            pbar.update(1)

    video_capture.release()

def main():
    parser = argparse.ArgumentParser(description='Extract frames from a video file')
    parser.add_argument('video_path', type=str, help='Path to the input video file')
    parser.add_argument('output_folder', type=str, help='Folder to save the extracted frames')
    parser.add_argument('frame_rate', type=int, help='Frame rate for extraction')
    args = parser.parse_args()

    extract_frames(args.video_path, args.output_folder, args.frame_rate)

if __name__ == "__main__":
    main()
