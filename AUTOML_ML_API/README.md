# Auto ML & ML APIs

GCP offers bunch of pre-trained models as well as AUTO ML capabilities for different type of data, In this we will explore & list down all the capabilities GCP offers.

# Products

| Data type	 | AutoML | Pre-trained models	|
| --- | --- | --- |
| Images | AutoML Vision | Vision API |
| Video | AutoML Video Intelligence | Video Intelligence API |
| Language: semantic analysis	 | AutoML Natural Language | Natural Language API & Healthcare Natural Language API |
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

# Video 
### AutoML Video
- **classification** : to classify shots and segments in the video
- **object tracking**: track multiple objects in shots and segments
### Video intellegence API
- identifies vast number of object,places & actions in stored as well as **streaming videos**
- **Label detection**: it does label detection in two ways.
  -	**At video level**: what is this video about 
  -	**At frame level**: what happening in every scene of video 
-	**Shot change detection**: if video changes from landscape pan to closeup it will detect that & give you timestamps for that
-	**Explicit content detection**: identify inappropriate scene from video 
-	**Object detection and tracking**: ex tracking a car in video. It will give you all timeframe where car is present 
-	**Person detection with pose estimation**
-	All other service which are present in Vision API is also available here.
-	We can also mention region where model should run. Benefits from low latency.


# Text
### AutoML Natural Language & Natural Language API
- it can classify documents(700 categories supported), entity extraction, sentiment analysis (can be detected at entity level) & analyzing text (Dependency parsing,Parsed label,POS tagging,Lemma,Morphology)
. all those features basic available in cloud Natural Language API. 
- AUTO ML lets you customize classification categories, entities, and sentiment scores that are relevant to your application
### Healthcare Natural Language
- **Healthcare Natural Language API** :
  - Extract information about medical concepts like diseases, medications, medical devices, procedures, and their clinically relevant attributes
  - Map medical concepts to standard medical vocabularies such as RxNorm, ICD-10, and MeSH
- **AutoML Entity Extraction for Healthcare** : specifically desinged for healthcare entity extraction


# Recommendation AI

### Steps to implement recommendation AI
- Import product catalog 
- Record user event 
- Determine recommendation Type & Placements

| Recommendation types	 | optimization objective | Available customizations|
| --- | --- | --- |
| Others You May Like | click-through rate | Change optimization objective to conversion rate </br> Add price reranking </br> Add diversification (supported but not recommended)|
| Frequently Bought Together  | revenue per order | Add diversification |
| Recommended for You  | click-through rate | Change optimization objective to conversion rate </br> Add price reranking </br> Add diversification |
| Recently Viewed  |  | It is not recommendation just user history |

### Optimization objectives

- Click-through rate (CTR): Optimizing for CTR emphasizes engagement; you should optimize for CTR when you want to maximize the likelihood that the user interacts with the recommendation.
- Revenue per order : The revenue per order optimization objective is the default optimization objective for the "Frequently Bought Together" recommendation model type 
- Conversion rate (CVR) : Optimizing for conversion rate maximizes the likelihood that the user adds the recommended item to their cart

### Advance options

- Diversification : If you want to ensure that results returned from a single prediction request are from different categories of your product catalog, you can enable diversification.Diversification reduces the likelihood that similar catalog items are shown in the recommendation panel, at the risk of removing some good recommendations.
- Price reranking: Price reranking causes recommended catalog items with a similar recommendation probability to be ordered by price, with the highest- priced items first.
- Results filtering : You can filter the prediction results for a placement by the tag value you provided with the catalog item and by whether the item is in stock
- Available placements: review statistics about where recommendations appear.




