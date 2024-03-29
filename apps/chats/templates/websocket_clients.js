document.addEventListener('DOMContentLoaded', function () {

    const messageContainer = document.querySelector('#message_container');
    const messageInput = document.querySelector('[name=message_input]');
    const sendMessageButton = document.querySelector('[name=send_message_button]');
    console.log(messageContainer);

    let websocketClient = new WebSocket('ws://localhost:12345');

    websocketClient.onopen = () => {
        console.log('Клиенты соединены!');

        sendMessageButton.onclick = () => {
            console.log(messageInput.value);
            websocketClient.send(messageInput.value);
            messageInput.value = '';
           
        };
    };

    websocketClient.onmessage = (message) => {
        const newMessage = document.createElement('div');
        console.log(message, 'dta');
        newMessage.innerText = message.data;
        messageContainer.appendChild(newMessage);

    };

}, false);
