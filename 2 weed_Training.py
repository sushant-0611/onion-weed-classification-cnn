from keras.layers import Conv2D,MaxPooling2D,Flatten,Dense
from keras.models import Sequential
import matplotlib.pyplot as plt

def plotHistory(history):
        
    # summarize history for accuracy
    fig = plt.figure(1)
    #fig.canvas.set_window_title("Model Accuracy Graph")
    plt.plot(history.history['accuracy'])
    plt.plot(history.history['val_accuracy'])
    plt.title('model accuracy')
    plt.ylabel('accuracy')
    plt.xlabel('epoch')
    plt.legend(['train', 'test'], loc='upper left')
    plt.show()
    # summarize history for loss
    fig = plt.figure(2)
    #fig.canvas.set_window_title("Model Loss Graph")
    plt.plot(history.history['loss'])
    plt.plot(history.history['val_loss'])
    plt.title('model loss')
    plt.ylabel('loss')
    plt.xlabel('epoch')
    plt.legend(['train', 'test'], loc='upper left')
    plt.show()
    


from keras.preprocessing.image import ImageDataGenerator
train_datagen = ImageDataGenerator(
        rescale=1./255,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True)

test_datagen = ImageDataGenerator(rescale=1./255)

training_set = train_datagen.flow_from_directory(
        'DATASET/train',
        target_size=(150,150),
        batch_size=64 ,
        class_mode='binary')

test_set = test_datagen.flow_from_directory(
        'DATASET/test',
        target_size=(150,150),
        batch_size=64,
        class_mode='binary')

cnn_neural_netrwork=Sequential()
cnn_neural_netrwork.add(Conv2D(32,(3,3),activation='relu',input_shape=(150,150,3)))#l1
cnn_neural_netrwork.add(MaxPooling2D() )

cnn_neural_netrwork.add(Conv2D(32,(3,3),activation='relu'))#L2
cnn_neural_netrwork.add(MaxPooling2D() )

cnn_neural_netrwork.add(Conv2D(32,(3,3),activation='relu'))#L3
cnn_neural_netrwork.add(MaxPooling2D() )

cnn_neural_netrwork.add(Conv2D(32,(3,3),activation='relu'))#L4
cnn_neural_netrwork.add(MaxPooling2D() )

cnn_neural_netrwork.add(Flatten())
cnn_neural_netrwork.add(Dense(100,activation='relu'))
cnn_neural_netrwork.add(Dense(1,activation='sigmoid'))

history=cnn_neural_netrwork.compile(optimizer='adam',loss='binary_crossentropy',metrics=['accuracy'])




history=cnn_neural_netrwork.fit_generator(
        training_set,
        epochs=50,
        validation_data=test_set,

        )

cnn_neural_netrwork.save('weed_trained_data.h5',history)
plotHistory(history)

print("==============================saved the model===============================================")
