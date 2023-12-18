const url = "ws://10.1.2.10:13337"

async function handle_client() {
    const socket = new WebSocket(url);

    const input = document.createElement("input");
    input.type = "text";
    input.placeholder = "Entrez un message";
    document.body.appendChild(input); 
    
    const messageDisplay = document.createElement("div");
    document.body.appendChild(messageDisplay);  

    input.addEventListener("keydown", (event) => {
        if (event.key === "Enter") {
            const message = input.value;
            socket.send(message);
            input.value = ""; 
            document.body.removeChild(input);
        }
    });

    socket.onopen = () => {
        console.log("Connexion WebSocket ouverte");
    };

    socket.onmessage = (event) => {
        const message = event.data

        const messageElement = document.createElement("p");
        messageElement.textContent = message;
        messageDisplay.appendChild(messageElement);
    };

    socket.onclose = () => {
        console.log("Connexion WebSocket fermée");
    };
}

handle_client();