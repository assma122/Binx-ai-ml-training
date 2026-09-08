# Week 8 — Day 3: Computer Vision Preprocessing

## Overview

This notebook focuses on building a complete computer vision preprocessing workflow using OpenCV and TensorFlow/Keras.

The goal is to transform raw images with different sizes, color representations, and pixel ranges into consistent model-ready inputs. The notebook also explores data augmentation, structural edge extraction, and model-specific preprocessing for transfer learning.

---

## Learning Objectives

By the end of this notebook, the following concepts are covered:

- Understand why image preprocessing is necessary
- Read and inspect images using OpenCV
- Resize images to a fixed input size
- Convert images from BGR to RGB
- Normalize pixel values
- Visualize the effect of preprocessing
- Apply grayscale conversion and Canny edge detection
- Build an image augmentation pipeline
- Match preprocessing to a pre-trained model
- Compare custom-model preprocessing with MobileNetV2 preprocessing
- Validate final model-ready image inputs

---

## Dataset

The notebook uses the TensorFlow Flowers dataset.

The dataset contains **3,670 images** distributed across five flower classes:

- Daisy
- Dandelion
- Roses
- Sunflowers
- Tulips

The images contain natural variation in dimensions, aspect ratios, lighting conditions, backgrounds, and composition, making the dataset suitable for preprocessing and augmentation experiments.

---

## Preprocessing Workflow

The main image preprocessing pipeline follows:

`Raw Image → Resize → BGR to RGB → Convert to float32 → Normalize → Model-Ready Input`

Images are standardized to:

- Input size: `224 × 224 × 3`
- Color format: `RGB`
- Data type: `float32`

For a custom computer vision model, pixel values are normalized to:

`0 → 1`

---

## Image Dimension Analysis

The original dataset contains images with different widths, heights, and aspect ratios.

A dimension-distribution scatter plot is used to compare the original image geometries with the selected target size of `224 × 224`.

This demonstrates why resizing is required before images can be grouped into consistent model input tensors.

---

## Pixel Normalization Analysis

A pixel-intensity histogram compares the image before and after normalization.

Before normalization:

`Pixel range: 0 → 255`

After normalization:

`Pixel range: 0 → 1`

The overall distribution remains similar while the numerical scale changes, showing that normalization preserves relative intensity patterns while producing a more consistent numerical representation.

---

## BGR vs. RGB

OpenCV reads color images in **BGR** order, while Matplotlib and many deep learning workflows expect **RGB**.

The notebook demonstrates the visual difference between:

- BGR interpreted incorrectly as RGB
- Correct BGR-to-RGB conversion

This highlights an important preprocessing issue because incorrect channel ordering may not produce a runtime error, but it can provide incorrect color information to the model.

---

## Structural Feature Extraction

The notebook also explores classical computer vision preprocessing using:

- Grayscale conversion
- Canny edge detection

Canny edge detection emphasizes strong image boundaries while suppressing much of the smooth background.

This provides a structural representation of the image that can be useful in classical computer vision applications.

---

## Data Augmentation

An augmentation pipeline is created using `ImageDataGenerator`.

The applied transformations include:

- Rotation
- Zoom
- Horizontal flipping
- Brightness variation

Several augmented versions of the same flower image are visualized to verify that the image changes while the original class identity remains recognizable.

Random augmentation is intended for training data only, while validation and test data should remain deterministic.

---

## Training Pipeline Integration

Two preprocessing routes are explored.

### Custom Model

`Augmentation → Rescale to 0–1`

### MobileNetV2

`Augmentation → MobileNetV2 preprocess_input()`

The two pipelines preserve the same image geometry while using different numerical representations.

---

## Transfer Learning and MobileNetV2

Pre-trained models require the same input representation that was used during their original training.

For MobileNetV2:

- Shape: `224 × 224 × 3`
- Data type: `float32`
- Expected numerical range: `-1 → 1`

This differs from the generic `0 → 1` normalization used for the custom model.

Therefore, preprocessing must be selected according to the architecture receiving the image.

---

## Final Model Input Routes

### Custom Model

`Read → Resize → BGR to RGB → Normalize to 0–1`

### MobileNetV2

`Read → Resize → BGR to RGB → preprocess_input() → -1 to 1`

Both routes produce:

- `224 × 224 × 3`
- `float32`

The main difference is the numerical preprocessing contract.

---

## Key Visualizations

The notebook includes:

- Flowers dataset preview
- Image dimension distribution
- Raw vs. preprocessed image comparison
- Pixel intensity distribution before and after normalization
- BGR vs. RGB comparison
- Grayscale and Canny edge visualization
- Augmentation gallery
- Generic normalization vs. MobileNetV2 comparison
- Input range visualization

---

## Tools and Libraries

- Python
- OpenCV
- NumPy
- Pandas
- Matplotlib
- TensorFlow
- Keras

---

## Conclusion

The notebook demonstrates that computer vision preprocessing is not limited to resizing images.

A complete pipeline must ensure consistency in:

- Geometry
- Color-channel order
- Numerical scale
- Training augmentation
- Model-specific preprocessing

The final workflow transforms raw and inconsistent images into reproducible, model-compatible inputs.

The key rule is:

**Keep preprocessing consistent between training and inference.**