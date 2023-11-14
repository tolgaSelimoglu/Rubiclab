import cv2


def take_pic(path, image_count):

    count = 0
    cap = cv2.VideoCapture(0) # 1
    cv2.namedWindow('Test')

    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    x = width // 3
    y = height // 3
    w = width // 3 # 4
    h = width // 3

    while count < image_count:

        ret, frame = cap.read()
        cv2.rectangle(frame, (x, y), (x + w, y + h), color=(0, 0, 255), thickness=4)
        cv2.imshow('Test', frame)

        if ord('s') == cv2.waitKey(1):
            img = cv2.imwrite(f'{path}cube_face{count}.jpg', frame)

            if img:
                print(f'{count + 1}. image captured')
                count = count + 1

    cap.release()
    cv2.destroyAllWindows()


def crop_images(path, image_count):

        for i in range(image_count):
            image = cv2.imread(f'{path}cube_face{i}.jpg')

            crop_coordinates = (x, y, w, h)

            cropped_image = image[crop_coordinates[1]:crop_coordinates[1] + crop_coordinates[3], crop_coordinates[0]:crop_coordinates[0] + crop_coordinates[2]]

            cv2.imwrite(f'{path}cube_face{i}.jpg', cropped_image)


def image_main(path):

    image_count = 6
    take_pic(path, image_count)
    crop_images(path, image_count)
