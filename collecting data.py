import cv2
import os

if not os.path.exists("data"):
    os.makedirs("data")
    os.makedirs("data/train")
    os.makedirs("data/test")

    os.makedirs("data/train/0")
    os.makedirs("data/train/1")
    os.makedirs("data/train/2")
    os.makedirs("data/train/3")
    os.makedirs("data/train/4")
    os.makedirs("data/train/5")
    os.makedirs("data/train/6")
    os.makedirs("data/train/7")
    os.makedirs("data/train/8")
    os.makedirs("data/train/9")

    os.makedirs("data/train/A")
    os.makedirs("data/train/B")
    os.makedirs("data/train/C")
    os.makedirs("data/train/D")
    os.makedirs("data/train/E")
    os.makedirs("data/train/F")
    os.makedirs("data/train/G")
    os.makedirs("data/train/H")
    os.makedirs("data/train/I")
    os.makedirs("data/train/J")
    os.makedirs("data/train/K")
    os.makedirs("data/train/L")
    os.makedirs("data/train/M")
    os.makedirs("data/train/N")
    os.makedirs("data/train/O")
    os.makedirs("data/train/P")
    os.makedirs("data/train/Q")
    os.makedirs("data/train/R")
    os.makedirs("data/train/S")
    os.makedirs("data/train/T")
    os.makedirs("data/train/U")
    os.makedirs("data/train/V")
    os.makedirs("data/train/W")
    os.makedirs("data/train/X")
    os.makedirs("data/train/Y")
    os.makedirs("data/train/Z")

    os.makedirs("data/test/0")
    os.makedirs("data/test/1")
    os.makedirs("data/test/2")
    os.makedirs("data/test/3")
    os.makedirs("data/test/4")
    os.makedirs("data/test/5")
    os.makedirs("data/test/6")
    os.makedirs("data/test/7")
    os.makedirs("data/test/8")
    os.makedirs("data/test/9")

    os.makedirs("data/test/A")
    os.makedirs("data/test/B")
    os.makedirs("data/test/C")
    os.makedirs("data/test/D")
    os.makedirs("data/test/E")
    os.makedirs("data/test/F")
    os.makedirs("data/test/G")
    os.makedirs("data/test/H")
    os.makedirs("data/test/I")
    os.makedirs("data/test/J")
    os.makedirs("data/test/K")
    os.makedirs("data/test/L")
    os.makedirs("data/test/M")
    os.makedirs("data/test/N")
    os.makedirs("data/test/O")
    os.makedirs("data/test/P")
    os.makedirs("data/test/Q")
    os.makedirs("data/test/R")
    os.makedirs("data/test/S")
    os.makedirs("data/test/T")
    os.makedirs("data/test/U")
    os.makedirs("data/test/V")
    os.makedirs("data/test/W")
    os.makedirs("data/test/X")
    os.makedirs("data/test/Y")
    os.makedirs("data/test/Z")

mode = 'test'
directory = 'data/'+mode+'/'

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)

    count = {'zero': len(os.listdir(directory+"/0")),
             'one': len(os.listdir(directory+"/1")),
             'two': len(os.listdir(directory+"/2")),
             'three': len(os.listdir(directory+"/3")),
             'four': len(os.listdir(directory+"/4")),
             'five': len(os.listdir(directory+"/5")),
             'six': len(os.listdir(directory+"/6")),
             'seven': len(os.listdir(directory+"/7")),
             'eight': len(os.listdir(directory+"/8")),
             'nine': len(os.listdir(directory+"/9")),
             'A': len(os.listdir(directory+"/A")),
             'B': len(os.listdir(directory+"/B")),
             'C': len(os.listdir(directory+"/C")),
             'D': len(os.listdir(directory+"/D")),
             'E': len(os.listdir(directory+"/E")),
             'F': len(os.listdir(directory+"/F")),
             'G': len(os.listdir(directory+"/G")),
             'H': len(os.listdir(directory+"/H")),
             'I': len(os.listdir(directory+"/I")),
             'J': len(os.listdir(directory+"/J")),
             'K': len(os.listdir(directory+"/K")),
             'L': len(os.listdir(directory+"/L")),
             'M': len(os.listdir(directory+"/M")),
             'N': len(os.listdir(directory+"/N")),
             'O': len(os.listdir(directory+"/O")),
             'P': len(os.listdir(directory+"/P")),
             'Q': len(os.listdir(directory+"/Q")),
             'R': len(os.listdir(directory+"/R")),
             'S': len(os.listdir(directory+"/S")),
             'T': len(os.listdir(directory+"/T")),
             'U': len(os.listdir(directory+"/U")),
             'V': len(os.listdir(directory+"/V")),
             'W': len(os.listdir(directory+"/W")),
             'X': len(os.listdir(directory+"/X")),
             'Y': len(os.listdir(directory+"/Y")),
             'Z': len(os.listdir(directory+"/Z")),
             }

    cv2.putText(frame, "MODE : "+mode, (10, 20), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,255), 1)
    cv2.putText(frame, "IMAGE COUNT", (10, 50), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,255), 1)
    cv2.putText(frame, "ZERO :"+str(count['zero']), (10, 70), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "ONE : "+str(count['one']), (10, 90), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "TWO : "+str(count['two']), (10, 110), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "THREE : "+str(count['three']), (10, 130), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "FOUR : "+str(count['four']), (10, 150), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "FIVE : "+str(count['five']), (10, 170), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "SIX : "+str(count['six']), (10, 190), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "SEVEN : "+str(count['seven']), (10, 210), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "EIGHT : "+str(count['eight']), (10, 230), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "NINE : "+str(count['nine']), (10, 250), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "A : "+str(count['A']), (10, 270), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "B : "+str(count['B']), (10, 290), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "C : "+str(count['C']), (10, 310), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "D : "+str(count['D']), (10, 330), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "E : "+str(count['E']), (10, 350), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "F : "+str(count['F']), (10, 370), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "G : "+str(count['G']), (10, 390), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "H : "+str(count['H']), (10, 410), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "I : "+str(count['I']), (10, 430), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "J : "+str(count['J']), (10, 450), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "K : "+str(count['K']), (10, 470), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "L : "+str(count['L']), (120, 70), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "M : "+str(count['M']), (120, 90), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "N : "+str(count['N']), (120, 110), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "O : "+str(count['O']), (120, 130), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "P : "+str(count['P']), (120, 150), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "Q : "+str(count['Q']), (120, 170), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "R : "+str(count['R']), (120, 190), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "S : "+str(count['S']), (120, 210), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "T : "+str(count['T']), (120, 230), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "U : "+str(count['U']), (120, 250), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "V : "+str(count['V']), (120, 270), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "W : "+str(count['W']), (120, 290), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "X : "+str(count['X']), (120, 310), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "Y : "+str(count['Y']), (120, 330), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "Z : "+str(count['Z']), (120, 350), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)


    x1 = int(0.7*frame.shape[1])
    y1 = 100
    x2 = frame.shape[1]-10
    y2 = int(0.5*frame.shape[1])

    cv2.rectangle(frame, (x1-1, y1-1), (x2+1, y2+1), (255,0,0) ,1)

    thresh = frame[y1:y2, x1:x2]
    thresh = cv2.resize(thresh, (64, 64))
    cv2.imshow("Frame", frame)

    thresh = cv2.cvtColor(thresh, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(thresh, 120, 255, cv2.THRESH_BINARY)
    cv2.imshow("thresh", thresh)
    
    interrupt = cv2.waitKey(10)
    if interrupt & 0xFF == 27:
        break
    if interrupt & 0xFF == ord('0'):
        cv2.imwrite(directory+'0/'+str(count['zero'])+'.jpg', thresh)
    if interrupt & 0xFF == ord('1'):
        cv2.imwrite(directory+'1/'+str(count['one'])+'.jpg', thresh)
    if interrupt & 0xFF == ord('2'):
        cv2.imwrite(directory+'2/'+str(count['two'])+'.jpg', thresh)
    if interrupt & 0xFF == ord('3'):
        cv2.imwrite(directory+'3/'+str(count['three'])+'.jpg', thresh)
    if interrupt & 0xFF == ord('4'):
        cv2.imwrite(directory+'4/'+str(count['four'])+'.jpg', thresh)
    if interrupt & 0xFF == ord('5'):
        cv2.imwrite(directory+'5/'+str(count['five'])+'.jpg', thresh)
    if interrupt & 0xFF == ord('6'):
        cv2.imwrite(directory+'6/'+str(count['six'])+'.jpg', thresh)
    if interrupt & 0xFF == ord('7'):
        cv2.imwrite(directory+'7/'+str(count['seven'])+'.jpg', thresh)
    if interrupt & 0xFF == ord('8'):
        cv2.imwrite(directory+'8/'+str(count['eight'])+'.jpg', thresh)
    if interrupt & 0xFF == ord('9'):
        cv2.imwrite(directory+'9/'+str(count['nine'])+'.jpg', thresh)
    if interrupt & 0xFF == 97:
        cv2.imwrite(directory+'A/'+str(count['A'])+'.jpg', thresh)
    if interrupt & 0xFF == 98:
        cv2.imwrite(directory+'B/'+str(count['B'])+'.jpg', thresh)
    if interrupt & 0xFF == 99:
        cv2.imwrite(directory+'C/'+str(count['C'])+'.jpg', thresh)
    if interrupt & 0xFF == 100:
        cv2.imwrite(directory+'D/'+str(count['D'])+'.jpg', thresh)
    if interrupt & 0xFF == 101:
        cv2.imwrite(directory+'E/'+str(count['E'])+'.jpg', thresh)
    if interrupt & 0xFF == 102:
        cv2.imwrite(directory+'F/'+str(count['F'])+'.jpg', thresh)
    if interrupt & 0xFF == 103:
        cv2.imwrite(directory+'G/'+str(count['G'])+'.jpg', thresh)
    if interrupt & 0xFF == 104:
        cv2.imwrite(directory+'H/'+str(count['H'])+'.jpg', thresh)
    if interrupt & 0xFF == 105:
        cv2.imwrite(directory+'I/'+str(count['I'])+'.jpg', thresh)
    if interrupt & 0xFF == 106:
        cv2.imwrite(directory+'J/'+str(count['J'])+'.jpg', thresh)
    if interrupt & 0xFF == 107:
        cv2.imwrite(directory+'K/'+str(count['K'])+'.jpg', thresh)
    if interrupt & 0xFF == 108:
        cv2.imwrite(directory+'L/'+str(count['L'])+'.jpg', thresh)
    if interrupt & 0xFF == 109:
        cv2.imwrite(directory+'M/'+str(count['M'])+'.jpg', thresh)
    if interrupt & 0xFF == 110:
        cv2.imwrite(directory+'N/'+str(count['N'])+'.jpg', thresh)
    if interrupt & 0xFF == 111:
        cv2.imwrite(directory+'O/'+str(count['O'])+'.jpg', thresh)
    if interrupt & 0xFF == 112:
        cv2.imwrite(directory+'P/'+str(count['P'])+'.jpg', thresh)
    if interrupt & 0xFF == 113:
        cv2.imwrite(directory+'Q/'+str(count['Q'])+'.jpg', thresh)
    if interrupt & 0xFF == 114:
        cv2.imwrite(directory+'R/'+str(count['R'])+'.jpg', thresh)
    if interrupt & 0xFF == 115:
        cv2.imwrite(directory+'S/'+str(count['S'])+'.jpg', thresh)
    if interrupt & 0xFF == 116:
        cv2.imwrite(directory+'T/'+str(count['T'])+'.jpg', thresh)
    if interrupt & 0xFF == 117:
        cv2.imwrite(directory+'U/'+str(count['U'])+'.jpg', thresh)
    if interrupt & 0xFF == 118:
        cv2.imwrite(directory+'V/'+str(count['V'])+'.jpg', thresh)
    if interrupt & 0xFF == 119:
        cv2.imwrite(directory+'W/'+str(count['W'])+'.jpg', thresh)
    if interrupt & 0xFF == 120:
        cv2.imwrite(directory+'X/'+str(count['X'])+'.jpg', thresh)
    if interrupt & 0xFF == 121:
        cv2.imwrite(directory+'Y/'+str(count['Y'])+'.jpg', thresh)
    if interrupt & 0xFF == 122:
        cv2.imwrite(directory+'Z/'+str(count['Z'])+'.jpg', thresh)

cap.release()
cv2.destroyAllWindows()

