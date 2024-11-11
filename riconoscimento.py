import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np

# Carica il modello addestrato
model = load_model('dogs_vs_cats_model.h5')

# Predizione di una nuova immagine
img_path = 'img/gatto.jpg'  # Cambia questo con il percorso della tua immagine
img = image.load_img(img_path, target_size=(150, 150))
img_array = image.img_to_array(img) / 255.0
img_array = np.expand_dims(img_array, axis=0)

prediction = model.predict(img_array)
if prediction[0] > 0.5:
    print("È un gatto!")
else:
    print("È un cane!")
