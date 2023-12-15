const url = "ws://10.1.1.10:13337"

async function handle_client(){
const webSocket = new WebSocket(url);

exampleSocket.send("Here's some text that the server is urgently awaiting!");

exampleSocket.onopen = () => {
    exampleSocket.send("Hello im open");
  };

exampleSocket.onmessage = (event) => {
console.log(event.data);
};

exampleSocket.onclose = () => {
    exampleSocket.send("closed");
  };

}