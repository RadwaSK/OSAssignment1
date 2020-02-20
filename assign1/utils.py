from os.path import join
import cv2
import os
import tqdm


def read_video(video_path):
    """
    Read input video
    :param video_path: path of the video
    :return: video instance
    """
    video = cv2.VideoCapture(video_path)
    return video

def resample_video_frames(in_fps, out_fps, in_path, out_path):
    """
    Re-sample video frames into images with different FPS
    :param in_fps: input frames per second
    :param out_fps: output (required) frames per second
    :param in_path: input path of the video
    :param out_path: output path of the folder of images
    :return:
    """

    # inputs and outputs parameters
    in_sample_rate = int(in_fps)
    out_sample_rate = int(out_fps)

    # some calculations
    sample_rate = out_sample_rate / in_sample_rate
    current_sample = sample_rate
    name = 0

    # video sampling
    video = read_video(in_path)
    frames_count = video.get(cv2.CAP_PROP_FRAME_COUNT)

    for i in tqdm.trange(int(frames_count)):
        ret, frame = video.read()
        if ret:
            if current_sample >= 1:
                new_image_path = join(out_path, 'F_' + str(name).zfill(9) + ".jpg")
                write_image(new_image_path, frame)
                current_sample -= 1

            current_sample += sample_rate
            name += 1

    video.release()
    print("\tfinished sampling.")

def resize_image(image, width=None, height=None, inter=cv2.INTER_AREA):
    """
    Resize image with given width or height, keeping aspect ration

    :param image: Input image
    :param width: Desired width
    :param height: Desired height
    :param inter: Type of desired interpolation

    :return: Resized image
    """

    # initialize the dimensions of the image to be resized and
    # grab the image size
    dim = None
    (h, w) = image.shape[:2]

    # if both the width and height are None, then return the
    # original image
    if width is None and height is None:
        return image

    # check to see if the width is None
    if width is None:
        # calculate the ratio of the height and construct the
        # dimensions
        r = height / float(h)
        dim = (int(w * r), height)

    # otherwise, the height is None
    else:
        # calculate the ratio of the width and construct the
        # dimensions
        r = width / float(w)
        dim = (width, int(h * r))

    # resize the image
    resized = cv2.resize(image, dim, interpolation=inter)

    # return the resized image
    return resized


def read_images(directory):
    """
    Read a set of images in a directory

    :param directory: Directory to read images from
    :return: List of images
    """
    files = os.listdir(directory)
    files.sort()
    images = []
    for file in files:
        path = os.path.join(directory, file)
        img = cv2.imread(path, flags=cv2.IMREAD_GRAYSCALE)
        images.append(img)
    return images, files


def write_image(img_path, img):
    """
    :param img_path: the path of the image
    :param img: the image itself
    :return: nothing
    """
    ret = cv2.imwrite(img_path, img)

