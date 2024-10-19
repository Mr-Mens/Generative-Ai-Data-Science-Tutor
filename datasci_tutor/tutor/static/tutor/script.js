document.addEventListener("DOMContentLoaded", function() {
    const chatBox = document.getElementById("chat-box");
    const userInput = document.getElementById("user-input");

    function addMessage(role, content) {
        const message = document.createElement("div");
        message.classList.add("message");
        message.classList.add(role);
        message.textContent = content;
        chatBox.appendChild(message);
        chatBox.scrollTop = chatBox.scrollHeight;
    }

    window.sendMessage = function() {
        const message = userInput.value.trim();
        if (message === "") return;

        addMessage("user", message);
        userInput.value = "";

        fetch("/tutor/tutor_response/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": getCSRFToken() 
            },
            body: JSON.stringify({ message: message })
        })
        .then(response => response.json())
        .then(data => {
            if (data.response) {
                addMessage("bot", data.response);
            } else if (data.error) {
                addMessage("bot", "Error: " + data.error);
            }
        })
        .catch(error => {
            console.error("Error:", error);
            addMessage("bot", "Error connecting to the server.");
        });
    };

    function getCSRFToken() {
        let cookieValue = null;
        const name = 'csrftoken';
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
});
