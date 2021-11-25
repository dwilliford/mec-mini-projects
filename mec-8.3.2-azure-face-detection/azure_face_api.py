import http.client, urllib.request, urllib.parse, urllib.error, base64

headers = {
    # Request headers
    # Use this content type when passing url parm instead of binary image
    'Content-Type': 'application/json',
    # Use below for passing image but didn't get it working
    #'Content-Type': 'application/octet-stream',
    #'Ocp-Apim-Subscription-Key': '{subscription key}',
    'Ocp-Apim-Subscription-Key': '37fc98749e224c70ba3f0fb7aac3f14a',
}

#print(headers)

attributes = \
    "age,gender,headpose,smile," + \
    "facialhair,glasses,emotion," + \
    "hair,makeup,occlusion,accessories," + \
    "blur,exposure,noise"

#,qualityforrecognition

#THIS WORKS
#attributes = "hair"
#print(attributes)

params = urllib.parse.urlencode({
    # Request parameters
    'returnFaceId': 'true',
    'returnFaceLandmarks': 'true',
    'returnFaceAttributes': attributes
 #   'recognitionModel': 'recognition_04',
 #   'returnRecognitionModel': 'false',
 #   'detectionModel': 'detection_03',
 #   'faceIdTimeToLive': '86400',
})

print(params)
#params = {'returnFaceId" : 'true'}

def get_base64_encoded_image(image_path):
    with open(image_path, "rb") as img_file:
        #return base64.b64encode(img_file.read()).decode('utf-8')
        return base64.b64encode(img_file.read())

#body = get_base64_encoded_image('c:/Users/Dave/git_repos/mec-mini-projects/mec-8.3.2-azure-face-detection/BHO2.jpg')

body = '{\"url\":\"https://i.natgeofe.com/k/271050d8-1821-49b8-bf0b-3a4a72b6384a/obama-portrait_.jpg?w=1200\"}'


try:
    #conn = http.client.HTTPSConnection('westus.api.cognitive.microsoft.com')
    conn = http.client.HTTPSConnection('mec-face-api.cognitiveservices.azure.com')
    conn.request("POST", "/face/v1.0/detect?%s" % params, body, headers)
    response = conn.getresponse()
    data = response.read()
    print(data)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))

