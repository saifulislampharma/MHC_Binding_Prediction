#this model is implented from the following paper
from keras.layers import Input,Dense,Conv2D,MaxPooling2D,Flatten
from keras.models import Model
def protein_prediction_model(shape=(1,13,20)):
    inp_seq=Input(shape=shape)
    x=Conv2D(filters=512,
             kernel_size=(1,2),
             padding="valid",
             activation='relu',
             name="conv_1")(inp_seq)
             
    x=MaxPooling2D((1,2),name="max_pool_1")(x)
    x=Conv2D(filters=512,
             kernel_size=(1,3),
             padding="valid",
             activation="relu",
             name="conv_2"
             )(x)
    x=Flatten()(x)
    x=Dense(400,activation="tanh",name="dense_1")(x)
    x=Dense(2,activation="sigmoid",name="dense_2")(x)
    model=Model(inputs=inp_seq,outputs=x)
    return model
model=protein_prediction_model()
model.summary()
