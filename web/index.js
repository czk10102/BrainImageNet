var server = require("./server");
var router = require("./router");
var requestHandlers = require("./requestHandlers");

var handle = {}
handle["/"] = requestHandlers.start;
handle["/start"] = requestHandlers.start;
handle["/upload"] = requestHandlers.upload;
handle["/upload2"] = requestHandlers.upload2;
handle["/uploadt"] = requestHandlers.uploadt;
handle["/email2"] = requestHandlers.email2;
handle["/email"] = requestHandlers.email;
handle["/show"] = requestHandlers.show;
handle["/images/DPABIlogo2.png"]= requestHandlers.logo;
handle["/logo"]= requestHandlers.logo;

server.start(router.route,handle);