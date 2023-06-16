import cv2
import mediapipe as mp
import numpy as np
from math import acos, degrees
import random

def palm_centroid(coordinates_list):
    coordinates = np.array(coordinates_list)
    centroid = np.mean(coordinates, axis=0)
    centroid = int(centroid[0]), int(centroid[1])
    return centroid

def fingers_up_down(hand_results, thumb_points, palm_points, fingertips_points, finger_base_points):
    fingers = None
    coordinates_thumb = []
    coordinates_palm = []
    coordinates_ft = []
    coordinates_fb = []
    for hand_landmarks in hand_results.multi_hand_landmarks:
        for index in thumb_points:
            x = int(hand_landmarks.landmark[index].x * width)
            y = int(hand_landmarks.landmark[index].y * height)
            coordinates_thumb.append([x, y])

        for index in palm_points:
            x = int(hand_landmarks.landmark[index].x * width)
            y = int(hand_landmarks.landmark[index].y * height)
            coordinates_palm.append([x, y])

        for index in fingertips_points:
            x = int(hand_landmarks.landmark[index].x * width)
            y = int(hand_landmarks.landmark[index].y * height)
            coordinates_ft.append([x, y])

        for index in finger_base_points:
            x = int(hand_landmarks.landmark[index].x * width)
            y = int(hand_landmarks.landmark[index].y * height)
            coordinates_fb.append([x, y])

        ##########################
        # Pulgar
        p1 = np.array(coordinates_thumb[0])
        p2 = np.array(coordinates_thumb[1])
        p3 = np.array(coordinates_thumb[2])

        l1 = np.linalg.norm(p2 - p3)
        l2 = np.linalg.norm(p1 - p3)
        l3 = np.linalg.norm(p1 - p2)

        # Calcular el ángulo
        to_angle = (l1**2 + l3**2 - l2**2) / (2 * l1 * l3)
        if int(to_angle) == -1:
            angle = 180
        else:
            angle = degrees(acos(to_angle))
        thumb_finger = np.array(False)
        if angle > 150:
            thumb_finger = np.array(True)

        ################################
        # Índice, medio, anular y meñique
        nx, ny = palm_centroid(coordinates_palm)
        cv2.circle(frame, (nx, ny), 3, (0, 255, 0), 2)
        coordinates_centroid = np.array([nx, ny])
        coordinates_ft = np.array(coordinates_ft)
        coordinates_fb = np.array(coordinates_fb)

        # Distancias
        d_centrid_ft = np.linalg.norm(coordinates_centroid - coordinates_ft, axis=1)
        d_centrid_fb = np.linalg.norm(coordinates_centroid - coordinates_fb, axis=1)
        dif = d_centrid_ft - d_centrid_fb
        fingers = dif > 0
        fingers = np.append(thumb_finger, fingers)

        mp_drawing.draw_landmarks(
            frame,
            hand_landmarks,
            mp_hands.HAND_CONNECTIONS,
            mp_drawing_styles.get_default_hand_landmarks_style(),
            mp_drawing_styles.get_default_hand_connections_style()
        )
    return fingers

def choose_action(state, epsilon):
    # Exploración o explotación
    if np.random.uniform(0, 1) < epsilon:
        action = np.random.randint(0, 3)  # Exploración: acción aleatoria
    else:
        action = np.argmax(Q[state])  # Explotación: acción con el mayor valor de Q
    return action

def get_winner(user_action, pc_action):
    # Piedra: 0, Papel: 1, Tijeras: 2
    if user_action == pc_action:
        return "Empate"
    elif (user_action == 0 and pc_action == 2) or (user_action == 1 and pc_action == 0) or (user_action == 2 and pc_action == 1):
        return "Ganaste"
    else:
        return "Perdiste"

def update_q_value(state, action, reward, alpha, gamma):
    next_state = action  # Próximo estado es la acción elegida
    Q[state, action] = (1 - alpha) * Q[state, action] + alpha * (reward + gamma * np.max(Q[next_state]))

def play_game():
    epsilon = 0.3  # Tasa de exploración
    alpha = 0.5  # Tasa de aprendizaje
    gamma = 0.9  # Factor de descuento

    print("¡Juguemos a piedra, papel, tijeras!")
    while True:
        # Elección del usuario
        print("Elige una opción:")
        for i, option in enumerate(OPTIONS):
            print(f"{i}: {option}")
        user_action = int(input("Opción: "))

        # Elección de la computadora
        pc_action = choose_action(user_action, epsilon)

        # Verificar el resultado y actualizar valores de Q
        winner = get_winner(user_action, pc_action)
        reward = 0
        if winner == "Ganaste":
            reward = 1
        elif winner == "Perdiste":
            reward = -1

        update_q_value(user_action, pc_action, reward, alpha, gamma)

        print(f"La computadora eligió: {OPTIONS[pc_action]}")
        print(f"Resultado: {winner}")
        print()

        play_again = input("¿Quieres jugar de nuevo? (s/n): ")
        if play_again.lower() != "s":
            break

# Opciones del juego
OPTIONS = ["Piedra", "Papel", "Tijeras"]

# Matriz Q inicializada a cero
Q = np.zeros((len(OPTIONS), len(OPTIONS)))

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# Pulgar
thumb_points = [1, 2, 4]

# Índice, medio, anular y meñique
palm_points = [0, 1, 2, 5, 9, 13, 17]
fingertips_points = [8, 12, 16, 20]
finger_base_points = [6, 10, 14, 18]

# FINGERS COMBINATIONS
TO_ACTIVATE = np.array([True, False, False, False, False])
# Piedra, papel, tijeras
PIEDRA = np.array([False, False, False, False, False])
PAPEL = np.array([True, True, True, True, True])
TIJERAS = np.array([False, True, True, False, False])

# REGLAS PIEDRA, PAPEL, TIJERAS (0, 1, 2)
WIN_GAME = ["02", "10", "21"]

pc_option = False  # Si la pc ha escogido o no
detect_hand = True

THRESHOLD = 10
THRESHOLD_RESTART = 50

count_like = 0
count_piedra = 0
count_papel = 0
count_tijeras = 0
count_restart = 0

# Images to show
image1 = cv2.imread("1.jpg")
image2 = cv2.imread("2.jpg")
image_winner = cv2.imread("3.jpg")
image_tie = cv2.imread("4.jpg")
image_loser = cv2.imread("5.jpg")
# Image to concat
imAux = image1

player = None

with mp_hands.Hands(
        model_complexity=1,
        max_num_hands=1,
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5) as hands:

    while True:
        ret, frame = cap.read()
        if ret == False:
            break
        frame = cv2.flip(frame, 1)
        height, width, _ = frame.shape
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(frame_rgb)

        if results.multi_hand_landmarks:
            fingers = fingers_up_down(results, thumb_points, palm_points, fingertips_points, finger_base_points)
            # print("fingers:", fingers)

            if detect_hand == True:
                if not False in (fingers == TO_ACTIVATE) and pc_option == False:
                    if count_like >= THRESHOLD:
                        pc = random.randint(0, 2)
                        print("pc:", pc)
                        pc_option = True
                        imAux = image2
                    count_like += 1

                if pc_option == True:
                    if not False in (fingers == PIEDRA):
                        if count_piedra >= THRESHOLD:
                            player = 0
                        count_piedra += 1
                    elif not False in (fingers == PAPEL):
                        if count_papel >= THRESHOLD:
                            player = 1
                        count_papel += 1
                    elif not False in (fingers == TIJERAS):
                        if count_tijeras >= THRESHOLD:
                            player = 2
                        count_tijeras += 1
        if player is not None:
            detect_hand = False
            if pc == player:
                imAux = image_tie
            else:
                if (str(player) + str(pc)) in WIN_GAME:
                    imAux = image_winner
                else:
                    imAux = image_loser
            count_restart += 1
            if count_restart > THRESHOLD_RESTART:
                pc_option = False
                detect_hand = True
                player = None

                count_like = 0
                count_piedra = 0
                count_papel = 0
                count_tijeras = 0
                count_restart = 0
                imAux = image1

        n_image = cv2.hconcat([imAux, frame])
        cv2.imshow("n_image", n_image)
        if cv2.waitKey(1) & 0xFF == 27:
            break
cap.release()
cv2.destroyAllWindows()
