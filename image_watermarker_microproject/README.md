# Watermark Images Application

This documentation explains a Python application that allows users to add text watermarks to images. Users can upload an image, add a text watermark, and save the watermarked image with the text added.

## Purpose
The purpose of this application is to provide a user-friendly interface for watermarking images with text. It allows users to customize and apply text watermarks to images and save the watermarked images.

## Dependencies
To run this application, you need the following dependencies:
- `customtkinter`: This module provides a custom extension of the `tkinter` library for GUI development.
- `tkinter.filedialog`: This module is used for opening and saving files through the file dialog.
- `shutil`: The `shutil` module is used for copying image files to the application's assets directory.
- `PIL` (Pillow): The Python Imaging Library is used for image processing, resizing, and adding text watermarks.
- `os`: The `os` module is used for file operations and cache cleanup.

## Usage
1. The application opens with a title and a "Upload Image" button, inviting users to upload an image.
2. Users can click the "Upload Image" button to select an image file (PNG format).
3. The selected image is copied to the "assets" directory for processing.
4. The image is displayed in the application's window, and users are prompted to enter the watermark text.
5. After entering the watermark text, the "Apply Watermark" button becomes enabled.
6. Users can click the "Apply Watermark" button to add the entered text as a watermark to the image.
7. The watermarked image is displayed, and users can click the "Save" button to save it.
8. After saving the watermarked image, a "Image Saved Successfully" message is displayed.
9. Users can clear the cache by closing the application, which removes the temporary image.

## Considerations
- The application is designed for adding text watermarks to images in PNG format.
- It provides a simple and user-friendly interface for this specific task.
- Users can customize the text watermark and save the watermarked image to their desired location.

## Security Considerations
- The application does not handle user authentication, but it does not require any sensitive information. Be cautious with the "confidential" information.
- The cache is cleared automatically when the application is closed, removing the temporary image.

## CustomTKinter
The script uses the `customtkinter` module, which is a custom extension of `tkinter` for creating a custom GUI. Ensure that this module is available and properly installed for the application to run.

## License
This application is provided for educational and personal use. Please respect any licensing and usage restrictions associated with the dependencies and image assets used in the application.

Enjoy watermarking your images with this user-friendly Python application!
