# !pip install cv2
import cv2
import random
import time
import pandas as pd

# Open the video file
low = 'low_Received.mp4'
medium= 'medium_Received.mp4'
high="high_Received.mp4"

# Open the video file
video_file ='low_Received.mp4'
cap = cv2.VideoCapture(video_file)

cap_L = cv2.VideoCapture(low)
cap_M=cv2.VideoCapture(medium)
cap_H=cv2.VideoCapture(high)


# Define the frame rate (frames per second) and duration (in seconds)
total_frames = int(cap_L.get(cv2.CAP_PROP_FRAME_COUNT))
frame_rate = cap.get(cv2.CAP_PROP_FPS)
fps = int(cap.get(cv2.CAP_PROP_FPS))
duration_seconds = total_frames / fps
duration = duration_seconds  

# Initialize lists to store lag length, lag ratio, and time data
lag_length_low_data = []
lag_length_medium_data = []
lag_length_high_data = []
lag_ratio_low_data = []
lag_ratio_medium_data = []
lag_ratio_high_data = []
time_data = []

# Simulate lag length and lag ratio over the specified duration
start_time = time.time()
current_time = start_time

while current_time - start_time < duration:
    # Capture the current frame
    ret, frame = cap.read()

    if not ret:
        break

    # Simulate lag length 
    lag_length_ms_L = random.uniform(100, 200)  # Adjust the range as needed
    lag_length_low_data.append(lag_length_ms_L)
    
    lag_length_ms_M = random.uniform(150, 300)  # Adjust the range as needed
    lag_length_medium_data.append(lag_length_ms_M)
    
    lag_length_ms_H = random.uniform(280, 500)  # Adjust the range as needed
    lag_length_high_data.append(lag_length_ms_H)

    # Simulate lag ratio (random values between 0 and 1)
    lag_ratio_L = random.uniform(0.45, 1.1)
    lag_ratio_low_data.append(lag_ratio_L)
    
    
    lag_ratio_M = random.uniform(1.0, 1.75)
    lag_ratio_medium_data.append(lag_ratio_M)
    
    lag_ratio_H = random.uniform(1.5, 2.5)
    lag_ratio_high_data.append(lag_ratio_H)

    # Store the current time
    time_data.append(current_time - start_time)

    # Display the frame (optional, for visual reference)
    cv2.imshow('Frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    # Wait for the frame rate interval
    time.sleep(1 / frame_rate)

    # Update current time
    current_time = time.time()

# Release the video capture object and close the display window
cap.release()
cv2.destroyAllWindows()

# Create a pandas DataFrame
data = {
    'Time (s)': time_data,
    'Lag Length of low quality (ms)': lag_length_low_data,
    'Lag Length of medium quality (ms)': lag_length_medium_data,
    'Lag Length of High quality (ms)': lag_length_high_data,
    'Lag Ratio of Low Video': lag_ratio_low_data,
    'Lag Ratio of Medium Video': lag_ratio_medium_data,
    'Lag Ratio of High Video': lag_ratio_high_data,
    
}
df = pd.DataFrame(data)

import matplotlib.pyplot as plt
import pandas as pd


# Create subplots for lag length and lag ratio
fig, axes = plt.subplots(2, 1, figsize=(12, 10))  # Adjust the figure size if needed
plt.rcParams.update({'font.size': 16})  # Increase the font size for all text

# Plot Lag Length
axes[0].plot(df['Time (s)'], df['Lag Length of low quality (ms)'], label='Low Quality', linestyle='-', marker='o', color='b')
axes[0].plot(df['Time (s)'], df['Lag Length of medium quality (ms)'], label='Medium Quality', linestyle='--', marker='s', color='g')
axes[0].plot(df['Time (s)'], df['Lag Length of High quality (ms)'], label='High Quality', linestyle='-.', marker='^', color='r')
axes[0].set_xlabel('Time (s)', fontsize=18)
axes[0].set_ylabel('Lag Length (ms)', fontsize=18)
axes[0].set_title('Lag Length Over Time for Different Video Quality Levels', fontsize=20)
axes[0].legend(fontsize=14)

# Plot Lag Ratio
axes[1].plot(df['Time (s)'], df['Lag Ratio of Low Video'], label='Low Quality', linestyle='-', marker='o', color='b')
axes[1].plot(df['Time (s)'], df['Lag Ratio of Medium Video'], label='Medium Quality', linestyle='--', marker='s', color='g')
axes[1].plot(df['Time (s)'], df['Lag Ratio of High Video'], label='High Quality', linestyle='-.', marker='^', color='r')
axes[1].set_xlabel('Time (s)', fontsize=18)
axes[1].set_ylabel('Lag Ratio', fontsize=18)
axes[1].set_title('Lag Ratio Over Time for Different Video Quality Levels', fontsize=20)
axes[1].legend(fontsize=14)

# Adjust spacing between subplots
plt.tight_layout()

# Show the plots
plt.show()