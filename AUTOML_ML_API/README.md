# Auto ML & ML APIs

GCP offers bunch of pre-trained models as well as AUTO ML capabilities for different type of data, In this we will explore & list down all the capabilities GCP offers.

# Products

| Data type	 | AutoML | Pre-trained models	|
| --- | --- | --- |
| Images | AutoML Vision | Vision API |
| Video | AutoML Video Intelligence | Video Intelligence API |
| Language: semantic analysis	 | AutoML Natural Language | Natural Language API & Healthcare Natural Language AI |
| Language: translation	 | AutoML Translation	 | Translation API Basic & Translation API Advanced |
| Chatbot	 | 	 | Dialogflow |
| Speech	 | 	 | Cloud Text-to-Speech API, Cloud Speech-to-Text API	 |
| Structured data : predictions | AutoML Tables	 | 	 |
| Structured data : recommendations	 | 	 | Recommendations AI	 |


# Images # Vision

- **OCR**: optical character recognition to extract text from images, give you coordinates where it is found as well as language of the text. it can detect dense text or handwritten
- **Logo detection** : identify companies’ logos in the image, it can search for logos of well-known companies.If the company is new or small use AutoML Vision
- **Landmark detection** : if image contains common landmark will also provide latitude and longitude of that landmark
- **Crop Hints**: helps you to crop the image to focus on particular subject
- **Explicit content detection** : provides likelihood ratings for the following explicit categories like adult, spoof, medical, violence & racy.
- **Image classification** : classify image using pre-defined labels. to train on custom labels use AUTO ML. if data is not labelled we can leverage Google’s data labeling service
- **web detection** : web detection is step further with label it will find similar images across web & extract text where image is found to give extra information about that image.
- **vision product search** : Compare photos to images in your product catalog, and return a ranked list of similar items.
- **Face detection** : detects face in image & facial attributes (like emotions).Face recognition not supported 
- **celebrity recognition**: Identify celebrity faces in images
- **AUTO ML edge**: allows you to train and deploy low-latency, high accuracy models optimized for edge devices. to build application on iOS or Android devices use AutoML Vision Edge in ML Kit
- **object localization** : detects multiple objects in an image & gives coordinates
