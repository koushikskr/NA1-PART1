var net = require('net');
var server = net.createServer();
server.on('connection', handleConnection);
server.listen(12029,'192.168.86.42', function() {
  console.log('Your server is now listening to %j', server.address());
});
server.maxConnections = 1;
function handleConnection(c) 
{  
  var Addr = c.remoteAddress + ':' + c.remotePort;
  console.log('You have a new client connection from the ipaddress %s', Addr);
  c.setEncoding('utf8');
  c.on('data', onConnData);
  c.once('close', onConnClose);
  c.on('error', onConnError);
function dataParse(str){
//console.log(str);
var k= JSON.parse(str);
//console.log("this is k",k.list);
var p=0;
var temp;
var temp1= " ";
for(var i=0;i< k.list.length;i++){
if((k.list[i].dt_txt).includes("09:00:00")){
if(p<=2){
console.log(k.list[i].dt_txt,k.list[i].main.temp+"F");
temp=k.list[i].dt_txt+" "+k.list[i].main.temp+"F";
temp1=temp1+temp +"\n";
p++;
}
}
}
 console.log(temp1);
c.write(temp1);
}

function onConnData(d) 
 {
    console.log('You are getting data from %s: %j', Addr, d);
    if(d=="weather" || d=="Weather"){
var XMLHttpRequest = require("xmlhttprequest").XMLHttpRequest;
var http= new XMLHttpRequest();

http.open("GET", "https://api.openweathermap.org/data/2.5/forecast?q=Kansas%20City&APPID=ea9e30eaf938bd9440a04c84fa57dd34");
http.send();

http.onload = () => dataParse(http.responseText)

     }
if (d != "Exit" && d!=="weather" && d!=="Weather")
    {
      c.write(d);
    }
    if (d == "Exit")
    {
      c.write(d);
      server.close();
    }
 }

function onConnClose() 
 {
    console.log('Your connection from the client %s closed', Addr);
 }

function onConnError(e) 
 {
  console.log('There is an error %s connection: %s', Addr, e.message);
 }
}
