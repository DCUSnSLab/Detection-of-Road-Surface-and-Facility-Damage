import cv2
import os
from tqdm import tqdm
from augment import write_images
from augment import augmentations

# 디렉터리 생성
def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)

    except OSError:
        print('Error: Creating directory. ' + directory)

# 영상 프레임 분할
def video_capture(video_file_path, video_name, image_path):
    # 영상 객체 생성
    vidcap = cv2.VideoCapture(video_file_path)
    # 객체 생성 확인
    if not vidcap.isOpened():
        print("Is not open")
        exit()

    count = 1

    while vidcap.isOpened():
        # 프레임 단위 이미지 읽기
        # success : 읽기 성공 여부
        # image : 이미지 저장
        success, image = vidcap.read()

        # 이미지 읽기 실패 여부
        if not success:
            break

        # 이미지 경로 저장
        img_name = video_name + '-' + str(count) + ".jpg"
        img_file_path = os.path.join(image_path, img_name)


        # 해당 경로에 이미지 저장
        print("img_file_path :", img_file_path)
        is_success, im_buf_arr = cv2.imencode(".jpg", image)
        im_buf_arr.tofile(img_file_path)

        # 증강 이미지 저장
        # augmentations(image, video_name, str(count))
        img_augmented = augmentations(image)
        write_images(image_path, video_name, str(count), img_augmented)

        # cv2.imwrite(image_file_path, image)

        print('Saved frame%d.jpg' % count)
        count += 1

    # 영상 객체 해제
    vidcap.release()


if __name__ == '__main__':
    # directory status
    dir_path = os.getcwd()

    # video & image folder name
    vid = "video"
    img = "image"

    # video folder path
    vid_dir = os.path.join(dir_path, vid)

    # video file list
    f_list = os.listdir(vid_dir)

    for x in f_list:
        # video file path
        vid_path = os.path.join(vid_dir, x)

        # 영상 파일명 확장자 분리
        vid_name = x.split('.')
        noEextension = vid_name[:-1]

        # Exception
        if (str(type(noEextension)) == "<class 'str'>"):
            video_name = noEextension
        else:
            video_name = '.'.join(noEextension)
        # Create directory each video
        img_dir = os.path.join(dir_path, img, video_name)
        createFolder(img_dir)
        createFolder(img_dir+"_aug")

        video_capture(vid_path, video_name, img_dir)
