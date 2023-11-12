import cv2


def take_pic(path):
    cap = cv2.VideoCapture(0)
    cv2.namedWindow('Test')

    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    x = width // 3
    y = height // 3

    w = width // 3
    h = width //3


    count = 0
    while count < 6:
        ret, frame = cap.read()

        cv2.rectangle(frame, (x, y), (x+w, y+h), color=(0,0,255),thickness= 4)

        cv2.imshow('Test', frame)

        if cv2.waitKey(1) & 0xFF == ord('s'):
            print("sa")
            img = cv2.imwrite(f'{path}cube_face{count}.jpg', frame)
            count += 1

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


    cap.release()
    cv2.destroyAllWindows()

    for i in range(6):
        image = cv2.imread(f'{path}cube_face{i}.jpg')

        crop_coordinates = (x, y, w, h)

        cropped_image = image[crop_coordinates[1]:crop_coordinates[1] + crop_coordinates[3], crop_coordinates[0]:crop_coordinates[0] + crop_coordinates[2]]

        cv2.imwrite(f'src/data/cube_face{i}.jpg', cropped_image)
