function ChatClient(type) {
    this.username = "nobody";
    this.socket = NaN;
    this.messageHandler = function(message) {
        console.log('Default handler, you really should change this!');
        console.log(message);
    };

    this.run = function() {
        that = this;
        this.socket = io.connect('http://localhost:5000/chat');
        this.socket.on('motd', function(data) {
            $("#chatLogs").empty();
            that.messageHandler(data);
        });

        this.socket.on('msg-out', function(data) {
           that.messageHandler(data);
        });

        // Start all handlers
        this.socket.on('users', this.userListHandler);
    };

    this.setUsername = function(username) {
        this.username = username;
        this.socket.emit('setUser', {'username': this.username});
    };

    this.sendMessage = function(message) {
        this.socket.emit('msg-in', {message: message, username: this.username});
    };

    this.userListHandler = function(data) {
        console.log('Default handler, you should change this!');
        console.log('New list of users: ' + data.message.users);
    }
}