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
    frame_count = cap.get(cv2.CAP_PROP_FRAME_COUNT)
    frame_time = frame_idx / frame_count
    cap.set(2, frame_time)
    ret, frame = cap.read()
    return frame
