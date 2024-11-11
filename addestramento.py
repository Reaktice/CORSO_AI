import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
import os

# Creazione delle cartelle per il dataset
base_dir = 'dataset'
train_dir = os.path.join(base_dir, 'train')
validation_dir = os.path.join(base_dir, 'validation')

os.makedirs(os.path.join(train_dir, 'dogs'), exist_ok=True)
os.makedirs(os.path.join(train_dir, 'cats'), exist_ok=True)
os.makedirs(os.path.join(validation_dir, 'dogs'), exist_ok=True)
os.makedirs(os.path.join(validation_dir, 'cats'), exist_ok=True)

# Verifica che le cartelle contengano immagini
if not any([os.listdir(os.path.join(train_dir, 'dogs')), os.listdir(os.path.join(train_dir, 'cats')),
            os.listdir(os.path.join(validation_dir, 'dogs')), os.listdir(os.path.join(validation_dir, 'cats'))]):
    print("Assicurati che le cartelle contengano immagini di cani e gatti.")
    exit()

# Definisci i parametri del modello
input_shape = (150, 150, 3)
batch_size = 32
epochs = 12

# Prepara i generatori di dati
train_datagen = ImageDataGenerator(rescale=1./255)
val_datagen = ImageDataGenerator(rescale=1./255)

train_generator = train_datagen.flow_from_directory(
    train_dir,
    target_size=(150, 150),
    batch_size=batch_size,
    class_mode='binary'
)

validation_generator = val_datagen.flow_from_directory(
    validation_dir,
    target_size=(150, 150),
    batch_size=batch_size,
    class_mode='binary'
)

# Costruisci il modello
model = Sequential([
    Conv2D(32, (3, 3), activation='relu', input_shape=input_shape),
    MaxPooling2D((2, 2)),
    Conv2D(64, (3, 3), activation='relu'),
    MaxPooling2D((2, 2)),
    Conv2D(128, (3, 3), activation='relu'),
    MaxPooling2D((2, 2)),
    Flatten(),
    Dropout(0.5),
    Dense(512, activation='relu'),
    Dense(1, activation='sigmoid')
])

# Compila il modello
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Addestra il modello
history = model.fit(
    train_generator,
    epochs=epochs,
    validation_data=validation_generator
)

# Salva il modello
model.save('dogs_vs_cats_model.h5')
