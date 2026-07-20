"""6. Perform basic video processing operations on the captured video
• Read captured video in python  and  display the video, in slow motion and in fast motion."""
import os
import cv2
from IPython.display import HTML, display

# Step 1: Define the path to your uploaded video file
input_video = "VIDEO EXP .mp4"

# Step 2: Define a function to modify video speed and re-encode for browser playback
def create_speed_variant(input_path, output_path, speed_factor):
    cap = cv2.VideoCapture(input_path)
    
    if not cap.isOpened():
        print(f"Error: Could not open video file '{input_path}'. Please check the filename.")
        return False
        
    # Get original video properties
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)
    
    # Adjust target frame rate based on speed factor
    new_fps = fps * speed_factor
    
    # Save a temporary file using raw OpenCV encoding
    temp_output = "temp_" + output_path
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(temp_output, fourcc, new_fps, (width, height))
    
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        out.write(frame)
        
    cap.release()
    out.release()
    
    # Re-encode using ffmpeg to standard H.264 web codec so HTML5 tags can view it
    os.system(f'ffmpeg -y -i "{temp_output}" -vcodec libx264 -f mp4 "{output_path}" -loglevel quiet')
    
    # Remove the temporary file
    if os.path.exists(temp_output):
        os.remove(temp_output)
    return True

# Step 3: Run processing if the file is found
if os.path.exists(input_video):
    print("Processing videos... Please wait standard re-encoding takes a few seconds.")
    
    # Generate Slow Motion (0.5x speed)
    create_speed_variant(input_video, "slow_motion.mp4", speed_factor=0.5)
    
    # Generate Fast Motion (2.0x speed)
    create_speed_variant(input_video, "fast_motion.mp4", speed_factor=2.0)
    
    # Prepare a web-friendly version of the original video for seamless rendering
    os.system(f'ffmpeg -y -i "{input_video}" -vcodec libx264 -f mp4 "web_original.mp4" -loglevel quiet')

    # Step 4: Display all three videos side-by-side using an HTML flex box
    html_code = """
    <div style="display: flex; gap: 15px; justify-content: center;">
        <div style="text-align: center;">
            <h4>Original Speed</h4>
            <video width="280" controls><source src="web_original.mp4" type="video/mp4"></video>
        </div>
        <div style="text-align: center;">
            <h4>Slow Motion (0.5x)</h4>
            <video width="280" controls><source src="slow_motion.mp4" type="video/mp4"></video>
        </div>
        <div style="text-align: center;">
            <h4>Fast Motion (2.0x)</h4>
            <video width="280" controls><source src="fast_motion.mp4" type="video/mp4"></video>
        </div>
    </div>
    """
    display(HTML(html_code))
else:
    print(f"Error: '{input_video}' not found. Please upload it to your Colab sidebar files tab and make sure the name matches perfectly.")
