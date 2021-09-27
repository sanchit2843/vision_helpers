import cv2

def frame_extract(path):
    vidObj = cv2.VideoCapture(path)
    success = 1

    while success:
        success, image = vidObj.read()
        if success:
            yield image

def extract_specific_frame_from_video(video_path, frame_idx):
    cap = cv2.VideoCapture(video_path)
    cap.set(1, frame_idx)
    ret, frame = cap.read()
    return frame
