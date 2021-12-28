from imgaug import augmenters as iaa
import cv2
import os

# image save
def write_images(path, name, number, images):
    for i in range(0, len(images)):
        img_aug_name = name + '-' + number + '-' + str(i) + ".jpg"
        img_aug_file_path = os.path.join(path + "_aug", img_aug_name)
        is_success, im_buf_arr = cv2.imencode(".jpg", images[i])
        im_buf_arr.tofile(img_aug_file_path)
    print("image saving complete")

# images augmentation
def augmentations(images):
    seq1 = iaa.Sequential(
        [iaa.AverageBlur(k=(2, 7)),
         iaa.MedianBlur(k=(3, 11))])
    seq2 = iaa.ChannelShuffle(p=1.0)
    seq3 = iaa.Dropout((0.05, 0.1), per_channel=0.5)
    seq4 = iaa.Sequential(
        [iaa.Add((-15, 15)),
         iaa.Multiply((0.3, 1.5))])

    img1 = seq1.augment_images(images)
    #cv2.imwrite("./image/image_sequential/"+)
    img2 = seq2.augment_images(images)

    img3 = seq3.augment_images(images)

    img4 = seq4.augment_images(images)
    list = [img1, img2, img3, img4]
    return list
