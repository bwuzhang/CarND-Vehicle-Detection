**Vehicle Detection Project**

The goals / steps of this project are the following:

* Perform a Histogram of Oriented Gradients (HOG) feature extraction on a labeled training set of images and train a classifier Linear SVM classifier
* Optionally, you can also apply a color transform and append binned color features, as well as histograms of color, to your HOG feature vector.
* Note: for those first two steps don't forget to normalize your features and randomize a selection for training and testing.
* Implement a sliding-window technique and use your trained classifier to search for vehicles in images.
* Run your pipeline on a video stream (start with the test_video.mp4 and later implement on full project_video.mp4) and create a heat map of recurring detections frame by frame to reject outliers and follow detected vehicles.
* Estimate a bounding box for vehicles detected.

[//]: # (Image References)
[hog_feature]: ./output_images/hog.jpg
[feature1]: ./output_images/feature1.jpg
[feature2]: ./output_images/feature2.jpg
[feature3]: ./output_images/feature3.jpg
[sliding_windows]: ./output_images/sliding_windows.jpg
[image1]: ./examples/car_not_car.png
[image2]: ./examples/HOG_example.jpg
[image3]: ./examples/sliding_windows.jpg
[image4]: ./examples/sliding_window.jpg
[image5]: ./examples/bboxes_and_heat.png
[image6]: ./examples/labels_map.png
[image7]: ./examples/output_bboxes.png
[video1]: ./project_video.mp4
[result]: ./output_images/result.png
[result0]: ./output_images/result_0.jpg
[result1]: ./output_images/result_1.jpg
[result2]: ./output_images/result_2.jpg
[result3]: ./output_images/result_3.jpg
[result4]: ./output_images/result_4.jpg
[final_result0]: ./output_images/final_result_0.jpg
[final_result1]: ./output_images/final_result_1.jpg
[final_result2]: ./output_images/final_result_2.jpg
[final_result3]: ./output_images/final_result_3.jpg
[final_result4]: ./output_images/final_result_4.jpg
[car]: ./output_images/image0000.png
[non-car]: ./output_images/extra1.png
## [Rubric](https://review.udacity.com/#!/rubrics/513/view) Points
### Here I will consider the rubric points individually and describe how I addressed each point in my implementation.  

---
### Writeup / README

#### 1. Provide a Writeup / README that includes all the rubric points and how you addressed each one.  You can submit your writeup as markdown or pdf.  [Here](https://github.com/udacity/CarND-Vehicle-Detection/blob/master/writeup_template.md) is a template writeup for this project you can use as a guide and a starting point.  

Please see project.ipynb for my code.

### Histogram of Oriented Gradients (HOG)

#### 1. Explain how (and identify where in your code) you extracted HOG features from the training images.

The code for this step is contained in the second code cell of the IPython notebook.  

I started by reading in all the `vehicle` and `non-vehicle` images.  Here is an example of one of each of the `vehicle` and `non-vehicle` classes:

![alt text][car]
![alt text][non-car]

I then explored different color spaces and different `skimage.hog()` parameters (`orientations`, `pixels_per_cell`, and `cells_per_block`).  I grabbed random images from each of the two classes and displayed them to get a feel for what the `skimage.hog()` output looks like.

Here is an example using the `YUV` color space and HOG parameters of `orientations=15`, `pixels_per_cell=(8, 8)`, `cells_per_block=(2, 2)` and `spacial_bin=32`:

![alt text][hog_feature]
![alt text][feature1]
![alt text][feature2]
![alt text][feature3]
#### 2. Explain how you settled on your final choice of HOG parameters.

I tried various combinations of parameters and see how they worked in the SVM training. Then I selected parameters with the best performance.

#### 3. Describe how (and identify where in your code) you trained a classifier using your selected HOG features (and color features if you used them).

I trained a linear SVM in part 3. I used 7500 images for both car and non-car categories for balanced training. Spacial features and histogram feature were added to increase the feature space. Each concatenated feature was normalized before training. And then I evaluated the classifier on 2760 test images.

### Sliding Window Search

#### 1. Describe how (and identify where in your code) you implemented a sliding window search.  How did you decide what scales to search and how much to overlap windows?

The code for sliding window can be found in part 4. I manually chose 5 different scales to cover different size of the cars appearing in the images. Each scale of boxes were also restricted to a certain vertical location to reduce computation time.  An example is at below:

![alt text][sliding_windows]

#### 2. Show some examples of test images to demonstrate how your pipeline is working.  What did you do to optimize the performance of your classifier?

Adding more features definitely increased the accuracy of my classifier. However this also dramatically increased inference time for each image. So I had to choose a low overlap rate for sliding windows, and heavily restrict the amount of area they cover.

![alt text][result]
---

### Video Implementation

#### 1. Provide a link to your final video output.  Your pipeline should perform reasonably well on the entire project video (somewhat wobbly or unstable bounding boxes are ok as long as you are identifying the vehicles most of the time with minimal false positives.)
Here's a [link to my video result](./project_video.mp4)


#### 2. Describe how (and identify where in your code) you implemented some kind of filter for false positives and some method for combining overlapping bounding boxes.

I recorded the positions of positive detections in each frame of the video.  From the positive detections I created a heatmap and then thresholded that map to identify vehicle positions.  I then used `scipy.ndimage.measurements.label()` to identify individual blobs in the heatmap.  I then assumed each blob corresponded to a vehicle.  I constructed bounding boxes to cover the area of each blob detected.  

Here's an example result showing the heatmap from a series of frames of video, the result of `scipy.ndimage.measurements.label()` and the bounding boxes then overlaid on the last frame of video:

### Here are five frames and their corresponding heatmaps:

![alt text][result0]
![alt text][result1]
![alt text][result2]
![alt text][result3]
![alt text][result4]

### Here is the output of `scipy.ndimage.measurements.label()` on the integrated heatmap and final predictions from all five frames:
![alt text][final_result0]
![alt text][final_result1]
![alt text][final_result2]
![alt text][final_result3]
![alt text][final_result4]

---

### Discussion

#### 1. Briefly discuss any problems / issues you faced in your implementation of this project.  Where will your pipeline likely fail?  What could you do to make it more robust?

VideoFileClip reads image into RGB format instead of BGR. It took me some time to figure this out.

There are some false positives in the project video. Adding vehicle tracking between different frames can reduce some noise in the predictions.
