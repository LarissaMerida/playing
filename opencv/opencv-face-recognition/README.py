
Para extrair conjunto de dados do rosto:

py extract_embeddings.py --dataset dataset  --embeddings output/embeddings.pickle  --detector face_detection_model  --embedding-model openface_nn4.small2.v1.t7

Para treinar:
py train_model.py --embeddings output/embeddings.pickle  --recognizer output/recognizer.pickle  --le output/le.pickle

Para reconhecer rostos:
py recognize.py --detector face_detection_model --embedding-model openface_nn4.small2.v1.t7 --recognizer output/recognizer.pickle --le output/le.pickle --image images/ashton.jpg

Para reconhecer em video:
py recognize_video.py --detector face_detection_model --embedding-model openface_nn4.small2.v1.t7 --recognizer output/recognizer.pickle --le output/le.pickle


pip install imutils
pip install scikit-learn