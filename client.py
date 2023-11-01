import requests

# Replace with the actual IP address and port of the server hosting the video
server_ip = '192.168.227.129'  # Replace with the server's IP address
server_port = 8080  # Replace with the server's port (typically 80 for HTTP)

video_url = f'http://{server_ip}:{server_port}/video.mp4'  # Adjust the URL as needed

response = requests.get(video_url)

if response.status_code == 200:
    with open('received_video.mp4', 'wb') as video_file:
        video_file.write(response.content)
    print('Video received successfully.')
else:
    print('Failed to retrieve the video.')
