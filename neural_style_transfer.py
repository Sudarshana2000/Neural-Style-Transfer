import argparse
import cv2
import numpy as np
import os
import time


def process(inputPath, outputPath):
    # model selection
    modelPath = "models"
    modelType = ["instance_norm", "eccv16"]
    print("Model Types: ", ' '.join(modelType))
    i = int(input("Enter Model Type [0-1]: "))
    modelName = os.listdir(modelPath+modelType[i])
    print("Model Names:\n", '\n'.join(modelName))
    j = int(input("Enter Model Name [0-{0}]: ".format(len(modelName)-1)))
    model = modelPath + modelType[i] + '/' + modelName[j]
    
    # load style transfer model
    net = cv2.dnn.readNetFromTorch(model)
    
    # input image pre-processing
    image = cv2.imread(inputPath)
    h,w = image.shape[:2]
    h = int((h/w)*600)
    w = 600
    image = cv2.resize(image,(w,h))
    
    # construct a blob from the image, set the input, and then perform a forward pass of the network
    blob = cv2.dnn.blobFromImage(image, 1.0, (w, h), (103.939, 116.779, 123.680), swapRB=False, crop=False)
    net.setInput(blob)
    start = time.time()
    output = net.forward()
    end = time.time()
    
    # output image post-processing
    output = output.reshape((3, output.shape[2], output.shape[3]))
    output[0] += 103.939
    output[1] += 116.779
    output[2] += 123.680
    output = np.clip(output, 0, 255)
    output = output.transpose(1, 2, 0)
    output = output.astype('uint8')
    
    # results
    print("[INFO] neural style transfer took {:.4f} seconds".format(end - start))
    imageName = os.path.basename(inputPath)
    cv2.imwrite(outputPath+modelName[j][:-3]+"_"+imageName, output)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('inputPath', help='Path to input image')
    parser.add_argument('outputPath', help='Path to output image directory')
    args = parser.parse_args()
    process(args.inputPath, args.outputPath)