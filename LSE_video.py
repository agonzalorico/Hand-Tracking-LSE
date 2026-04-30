import cv2
import mediapipe as mp
import math
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

#Start the Video Camera (0 is the default but it might be changed)
cap = cv2.VideoCapture(0) 

#The model for handtracking is loaded
base_options = python.BaseOptions(
    model_asset_path="C:/Users/Portatil/Desktop/HandTracking/hand_landmarker.task"
)

options = vision.HandLandmarkerOptions(
    base_options=base_options,
    num_hands=1
)

detector = vision.HandLandmarker.create_from_options(options)

#The connections are defined, they connect some points to make the skeleton of the hand
HAND_CONNECTIONS = [
    (0,1),(1,2),(2,3),(3,4),
    (0,5),(5,6),(6,7),(7,8),
    (5,9),(9,10),(10,11),(11,12),
    (9,13),(13,14),(14,15),(15,16),
    (13,17),(17,18),(18,19),(19,20),(0,17)
]

#This function detects if two points (tip1 and tip2) are touching, it can be adjusted changing the value compared with the distance
def tips_touching(tip1, tip2):
    
    x1 = int(hand_landmarks[tip1].x * frame.shape[1])
    x2 = int(hand_landmarks[tip2].x * frame.shape[1])
    y1 = int(hand_landmarks[tip1].y * frame.shape[0])
    y2 = int(hand_landmarks[tip2].y * frame.shape[0])
    distance = int(math.sqrt(((y1-y2)**2)+((x1-x2)**2)))

    if distance<30:
        return True
    else:
        return False

#This function finds the distance between 2 points
def get_distance(point1, point2):
    x1 = int(hand_landmarks[point1].x * frame.shape[1])
    x2 = int(hand_landmarks[point2].x * frame.shape[1])
    y1 = int(hand_landmarks[point1].y * frame.shape[0])
    y2 = int(hand_landmarks[point2].y * frame.shape[0])
    distance = int(math.sqrt(((y1-y2)**2)+((x1-x2)**2)))
    return distance

#This sets of function check the points of the hand and  compare them with some conditions to see if they are the letter investigated
#This is not very efficient and should be changed in the future, maybe combining all of them or just a few into a single function
#The comparison of hand_landmarks might also be modified, putting them into a separate function with a clearer explanation of what is comparing
def check_A():

    if hand_landmarks[3].y < hand_landmarks[5].y:
        tip_ids = [8, 12, 16, 20]

        for tip in tip_ids:
            if hand_landmarks[tip].x > hand_landmarks[tip - 2].x:
                pass
            else:
                return False
        return True    
    else: return False

def check_B():

    if hand_landmarks[3].y < hand_landmarks[5].y:
        tip_ids = [8, 12, 16, 20]
        for tip in tip_ids:
            if hand_landmarks[tip].x < hand_landmarks[tip - 2].x:
                pass
            else:
                return False
        return True    
    else: return False

def check_D():
    touching = tips_touching(4,12)
    if touching == True and hand_landmarks[8].y < hand_landmarks[8 - 2].y:
        return True
    else:
        return False
    
def check_C():
    touching = tips_touching(8,20)
    distanciax = (hand_landmarks[0].x * frame.shape[1]) - (hand_landmarks[20].x*frame.shape[1])
    if hand_landmarks[8].x < hand_landmarks[6].x and hand_landmarks[8].y < hand_landmarks[4].y and touching == True and distanciax >10:
        return True
    else: return False
def check_E():
    distanciax = (hand_landmarks[0].x * frame.shape[1]) - (hand_landmarks[20].x*frame.shape[1])
    if hand_landmarks[2].y > hand_landmarks[5].y and hand_landmarks[3].x < hand_landmarks[10].x and distanciax <10:
        tip_ids = [8, 12, 16, 20]
        for tip in tip_ids:
            if hand_landmarks[tip].y > hand_landmarks[tip - 1].y:
                pass
            else:
                return False
        return True    
    else: return False

def check_F():
    tips = [12, 16, 20]
    for i in tips:
        if hand_landmarks[i].y < hand_landmarks[i-2].y:
            pass
        else: return False 
    if hand_landmarks[8].x < hand_landmarks[4].x and hand_landmarks[8].z <hand_landmarks[4].z:
        return True
    else: return False

def check_I():
    if hand_landmarks[2].x < hand_landmarks[17].x and hand_landmarks[8].y > hand_landmarks[8-2].y:
        if hand_landmarks[20].y < hand_landmarks[20-2].y and hand_landmarks[16].y > hand_landmarks[16-2].y:
            return True
        else: return False
    else: return False

def check_K():
    if hand_landmarks[8].x>hand_landmarks[8-2].x or hand_landmarks[12].x>hand_landmarks[12-2].x:
        return False
    if hand_landmarks[4].y < hand_landmarks[12].y and hand_landmarks[4].y > hand_landmarks[8].y and hand_landmarks[4].x > hand_landmarks[8].x :
        return True
    else: return False

def check_L():
    touching = tips_touching(4,12)
    if hand_landmarks[4].y<hand_landmarks[10].y:
        return False
    tips = [12,16,20]
    for i in tips:
        if hand_landmarks[i].y < hand_landmarks[i].y:
            return False
    if hand_landmarks[4].x < hand_landmarks[2].x and hand_landmarks[8].y < hand_landmarks[8-2].y and hand_landmarks[4].x < hand_landmarks[8].x:                
        if touching == False:
            return True
    return False
def check_M():
    tips = [8,12,16]
    for i in tips:
        if hand_landmarks[i].y > hand_landmarks[i-2].y:
            pass
        else: return False
    if hand_landmarks[20].y < hand_landmarks[14].y and hand_landmarks[5].y > hand_landmarks[1].y:
        return True
    else: return False

def check_N():
    tips = [8,12]
    for i in tips:
        if hand_landmarks[i].y > hand_landmarks[i-2].y:
            pass
        else: return False
    if hand_landmarks[16].y > hand_landmarks[16-2].y:
        return False
    elif hand_landmarks[20].y < hand_landmarks[14].y and hand_landmarks[5].y > hand_landmarks[1].y:
        return True
    else: return False
def check_O():
    touching = tips_touching(4,8)
    if touching == True and hand_landmarks[12].y < hand_landmarks[12 - 2].y:
        return True
    else:
        return False  
def check_P():
    tips = [8,12,16]
    distance1 = get_distance(8,12)
    for i in tips:
        if hand_landmarks[i].y < hand_landmarks[i-2].y and distance1<50:
            pass
        else: return False
    if hand_landmarks[20].y > hand_landmarks[14].y and hand_landmarks[5].y < hand_landmarks[1].y:
        return True
    else: return False 
def check_Q():
    tips = [8,12,16,20]
    for i in tips:
        if hand_landmarks[i].y < hand_landmarks[i-2].y:
            pass
        else: return False
    if hand_landmarks[20].x < hand_landmarks[8].x and hand_landmarks[4].x < hand_landmarks[5].x:
        return True
    else: return False

def check_R():
    if hand_landmarks[8].x > hand_landmarks[12].x and hand_landmarks[6].x < hand_landmarks[10].x and hand_landmarks[8].y < hand_landmarks[8-2].y:
        return True
    else:return False
def check_S():
    tips = [12, 16, 20]
    for i in tips:
        if hand_landmarks[i].y < hand_landmarks[i-2].y:
            pass
        else: return False 
    if hand_landmarks[8].x >hand_landmarks[3].x and hand_landmarks[8].y >hand_landmarks[5].y:
        return True
    else: return False
def check_U():
    tips = [8,12]
    for i in tips:
        if hand_landmarks[i].y < hand_landmarks[i-2].y:
            pass
        else: return False
    if hand_landmarks[16].y < hand_landmarks[16-2].y or hand_landmarks[8].x>hand_landmarks[12].x:
        return False
    elif hand_landmarks[20].y > hand_landmarks[14].y and hand_landmarks[5].y < hand_landmarks[1].y:
        return True
    else: return False

def check_W():
    tips = [8,12,16]
    distance1 = get_distance(8,12)
    for i in tips:
        if hand_landmarks[i].y < hand_landmarks[i-2].y and distance1>50:
            pass
        else: return False
    if hand_landmarks[20].y > hand_landmarks[14].y and hand_landmarks[5].y < hand_landmarks[1].y:
        return True
    else: return False
def check_G():
    tip_ids = [12, 16, 20]
    if hand_landmarks[8].x<hand_landmarks[8-2].x:
        pass
    else: return False
    for tip in tip_ids:
        if hand_landmarks[tip].x > hand_landmarks[tip - 2].x:
            pass
        else:
            return False
    return True   


#This is the main loop
while True:
    ret, frame = cap.read()
    if not ret:
        break

    #The image is flipped to get a mirror effect
    frame = cv2.flip(frame, 1)

    #image is converted into an rgb, because mediapipe works with this format
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    #The image is converted into a mp image object
    mp_image = mp.Image(
        image_format=mp.ImageFormat.SRGB,
        data=frame_rgb
    )

    #Detect hands
    result = detector.detect(mp_image)

    #if result.hand_lanmarks == True (A hand has been detected)
    if result.hand_landmarks:
        for hand_landmarks in result.hand_landmarks:

            #Draw the points in the video
            for landmark in hand_landmarks:
                x = int(landmark.x * frame.shape[1])
                y = int(landmark.y * frame.shape[0])
                cv2.circle(frame, (x, y), 5, (0, 255, 0), -1)

            #Draw the lines in the video
            for start, end in HAND_CONNECTIONS:
                x1 = int(hand_landmarks[start].x * frame.shape[1])
                y1 = int(hand_landmarks[start].y * frame.shape[0])

                x2 = int(hand_landmarks[end].x * frame.shape[1])
                y2 = int(hand_landmarks[end].y * frame.shape[0])

                cv2.line(frame, (x1, y1), (x2, y2), (255, 0, 0), 2)
            #A variable is created for each letter, with a value of True or False, this might be changed in the future to a unique variable that gets a string
            leterA = check_A()
            leterB = check_B()
            leterC = check_C()
            leterD = check_D()
            leterE = check_E()
            leterF = check_F()
            leterG = check_G()
            leterI = check_I()
            leterK = check_K()
            leterL= check_L()
            leterM = check_M()
            leterN = check_N()
            leterO = check_O()
            leterP = check_P()
            leterQ = check_Q()
            leterR = check_R()
            leterS= check_S()
            leterU = check_U()
            leterW = check_W()

            letras_diccionario = {"A":leterA, "B":leterB,"C":leterC, "D":leterD, "E":leterE,"F":leterF,
                                   "G":leterG, "I":leterI, "K":leterK, "L":leterL, "M":leterM, "N":leterN,
                                   "O":leterO, "P":leterP,"Q":leterQ, "R":leterR,"S":leterS, "U":leterU, "W":leterW}

            for letra, valor in letras_diccionario.items():
                if valor == True:
                    #print(letra)
                    cv2.putText(frame, f"Letra: {letra}", (20, 60),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1.5, (0, 255, 0), 3) 

    cv2.putText(frame, f"Para salir pulsa la tecla q", (0, 450),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.5, (0, 0, 255), 1)
    #The video is shown onscreen
    cv2.imshow("Hand Tracking", frame)

   #To exit the porgram you have press the letter q
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

#End the program
cap.release()
cv2.destroyAllWindows()