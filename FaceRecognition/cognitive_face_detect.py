#!/usr/bin/python
import cognitive_face as CF
import json
from os import path

apiKey = "FACE API SUBSCRIPTION KEY"  # Replace with a valid Subscription Key here.
CF.Key.set(apiKey)

img_url = path.join(path.dirname(path.realpath(__file__)), "detection1.jpg")
result = CF.face.detect(img_url,attributes = 'age,gender,headPose,smile,facialHair,glasses,emotion,hair,makeup,occlusion,accessories,blur,exposure,noise')
print(json.dumps(result,indent = 4))