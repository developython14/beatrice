const roomName = JSON.parse(document.getElementById('room-name').textContent);

const chatSocket = new WebSocket(
            'ws://'
            + window.location.host
            + '/ws/screen/home/'
            + roomName
            + '/'
        );


        chatSocket.onmessage = function(e) {
            const data = JSON.parse(e.data);
            console.log(data);
            document.querySelector('#chat-log').value += (data.message + '\n');
        };

        chatSocket.onclose = function(e) {
            console.error('Chat socket closed unexpectedly');
        };
 

        document.querySelector('#chat-message-input').focus();
        document.querySelector('#chat-message-input').onkeyup = function(e) {
            if (e.keyCode === 13) {  // enter, return
                document.querySelector('#chat-message-submit').click();
            }
        };

        document.querySelector('#chat-message-submit').onclick = function(e) {
            const messageInputDom = document.querySelector('#chat-message-input');
            const message = messageInputDom.value;
            chatSocket.send(JSON.stringify({
                'message': message
            }));
            messageInputDom.value = '';
        };






        document.addEventListener("DOMContentLoaded", () => {
            var but = document.getElementById("but");
            var video = document.getElementById("vid");
            var video1 = document.getElementById("vid1");
            var mediaDevices = navigator.mediaDevices;
            vid.muted = true;
            but.addEventListener("click", () => {
      
              // Accessing the user camera and video.
              mediaDevices
                .getUserMedia({
                  video: true,
                  audio: true,
                })
                .then((stream) => {
      
                  // Changing the source of video to current stream.
                  video.srcObject = stream;
                  video1.srcObject = stream;
                  video.addEventListener("loadedmetadata", () => {
                    video.play();
                  });
                  video1.addEventListener("loadedmetadata", () => {
                    video1.play();
                  });
                })
                .catch(alert);
            });
          });