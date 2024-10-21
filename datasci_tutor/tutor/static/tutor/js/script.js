
document.addEventListener("DOMContentLoaded", function() {
    const chatBox = document.getElementById("chat-box");
    const userInput = document.getElementById("user-input");

    // Create a Showdown converter instance
    const converter = new showdown.Converter();

    function addMessage(role, content) {
        const message = document.createElement("div");
        message.classList.add("message");
        message.classList.add(role);

        // Convert Markdown content to HTML if it's from the bot
        if (role === "bot") {
            const htmlContent = converter.makeHtml(content);
            message.innerHTML = htmlContent;
        } else {
            message.textContent = content;
        }

        chatBox.appendChild(message);
        chatBox.scrollTop = chatBox.scrollHeight;
    }

    // Attach `sendMessage` directly to the `window` object to make it globally accessible
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

     // Attach `selectTopic` directly to the `window` object
    window.selectTopic = function(topic) {
        addMessage("user", `I want to learn about ${topic}`);
        sendMessage(`Tell me about ${topic}`);
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
