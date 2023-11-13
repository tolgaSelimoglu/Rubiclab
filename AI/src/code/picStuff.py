
import cv2

def take_pic(path):
    count = 0

    def capture_frame(frame):
        nonlocal count
        cv2.imwrite(f"{path}cube_face{count}.jpg", frame)
        count += 1
        print(f"Captured image {count}")

    cap = cv2.VideoCapture(1)
    cv2.namedWindow('Test')

    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    x = width // 3
    y = height // 3
    w = width // 4
    h = width // 3

    while True:
        ret, frame = cap.read()
        cv2.rectangle(frame, (x, y), (x + w, y + h), color=(0, 0, 255), thickness=4)
        cv2.imshow('Test', frame)

        key = cv2.waitKey(1)
        if key == ord('s'):
            print("AA   ")
            if count != 6:
                #print("!!")
                img = cv2.imwrite(f'{path}cube_face{count}.jpg', frame)
                #print(img)
                if img:
                    
                    count = count + 1
                    print(count)
        elif key == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

    for i in range(6):
        image = cv2.imread(f'{path}cube_face{i}.jpg')

        crop_coordinates = (x, y, w, h)

        cropped_image = image[crop_coordinates[1]:crop_coordinates[1] + crop_coordinates[3], crop_coordinates[0]:crop_coordinates[0] + crop_coordinates[2]]

        cv2.imwrite(f'src/data/cube_face{i}.jpg', cropped_image)
