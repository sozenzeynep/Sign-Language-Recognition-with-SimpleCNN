from keras.models import model_from_json
import operator
import cv2

json_file = open("model-bw.json", "r")
model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(model_json)

loaded_model.load_weights("model-bw.h5")
print("Loaded model from disk")

cap = cv2.VideoCapture(0)

categories = {0: 'ZERO',
              1: 'ONE',
              2: 'TWO',
              3: 'THREE',
              4: 'FOUR',
              5: 'FIVE',
              6: "SIX",
              7: "SEVEN",
              8: "EIGHT",
              9: "NINE",
              'A': "A",
              'B': "B",
              'C': "C",
              'D': "D",
              'E': "E",
              'F': "F",
              'G': "G",
              'H': "H",
              'I': "I",
              'J': "J",
              'K': "K",
              'L': "L",
              'M': "M",
              'N': "N",
              'O': "O",
              'P': "P",
              'Q': "Q",
              'R': "R",
              'S': "S",
              'T': "T",
              'U': "U",
              'V': "V",
              'W': "W",
              'X': "X",
              'Y': "Y",
              'Z': "Z"
              }

while True:
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)

    x1 = int(0.7*frame.shape[1])
    y1 = 100
    x2 = frame.shape[1]-10
    y2 = int(0.5*frame.shape[1])

    cv2.rectangle(frame, (x1-1, y1-1), (x2+1, y2+1), (255,0,0) ,1)
    thresh = frame[y1:y2, x1:x2]

    thresh = cv2.resize(thresh, (64, 64))
    thresh = cv2.cvtColor(thresh, cv2.COLOR_BGR2GRAY)
    _, test_image = cv2.threshold(thresh, 120, 255, cv2.THRESH_BINARY)
    cv2.imshow("test", test_image)

    result = loaded_model.predict(test_image.reshape(1, 64, 64, 1))

    prediction = {'ZERO': result[0][0], 
                  'ONE': result[0][1], 
                  'TWO': result[0][2],
                  'THREE': result[0][3],
                  'FOUR': result[0][4],
                  'FIVE': result[0][5],
                  'SIX': result[0][6],
                  'SEVEN': result[0][7],
                  'EIGHT': result[0][8],
                  'NINE': result[0][9],
                  'A': result[0][10],
                  'B': result[0][11],
                  'C': result[0][12],
                  'D': result[0][13],
                  'E': result[0][14],
                  'F': result[0][15],
                  'G': result[0][16],
                  'H': result[0][17],
                  'I': result[0][18],
                  'J': result[0][19],
                  'K': result[0][20],
                  'L': result[0][21],
                  'M': result[0][22],
                  'N': result[0][23],
                  'O': result[0][24],
                  'P': result[0][25],
                  'Q': result[0][26],
                  'R': result[0][27],
                  'S': result[0][28],
                  'T': result[0][29],
                  'U': result[0][30],
                  'V': result[0][31],
                  'W': result[0][32],
                  'X': result[0][33],
                  'Y': result[0][34],
                  'Z': result[0][35],
                  }

    prediction = sorted(prediction.items(), key=operator.itemgetter(1), reverse=True)
    

    cv2.putText(frame, prediction[0][0], (500, 70), cv2.FONT_HERSHEY_PLAIN, 1, (255,0,0), 1)
    cv2.imshow("Frame", frame)
    
    interrupt = cv2.waitKey(10)
    if interrupt & 0xFF == 27:
        break
        
 
cap.release()
cv2.destroyAllWindows()
