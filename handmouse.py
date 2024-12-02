import cv2, mediapipe, pyautogui


detect_hand = mediapipe.solutions.hands.Hands()
draw_setting = mediapipe.solutions.drawing_utils
screen_x, screen_y = pyautogui.size()

kamera = cv2.VideoCapture(0)

x1 = y1 = x2 = y2 = 0
while True:
    _, view = kamera.read()

    tinggi_view, lebar_view, _ = view.shape
    view = cv2.flip(view, 1)

    rgb_view = cv2.cvtColor(view, cv2.COLOR_BGR2RGB)
    out_hand = detect_hand.process(rgb_view)
    all_hand = out_hand.multi_hand_landmarks

    if all_hand:
        for i in all_hand:
            draw_setting.draw_landmarks(view, i)
            satu_tangan = i.landmark
            for id, ln in enumerate(satu_tangan):
                x = int(ln.x * lebar_view)
                y = int(ln.y * tinggi_view)
                #print(x, y)

                if id == 7:
                    mouse_x = (screen_x / lebar_view * x)
                    mouse_y = (screen_y / tinggi_view * y)
                    cv2.circle(view, (x,y), 10, (0, 225, 225))
                    pyautogui.moveTo(mouse_x, mouse_y, duration=0.000000001)
                    x1 = x
                    y1 = y
                if id == 3:
                    x2 = x
                    y2 = y
                    cv2.circle(view, (x,y), 10, (0, 225, 225))

        jarak = y2 - y1
        print(jarak)
        if(jarak < 20):
            pyautogui.click()

    cv2.imshow("Kamera aktif", view)
    key = cv2.waitKey(100)
    if key == 27:
        break

kamera.release()
cv2.destroyAllWindows()