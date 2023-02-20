var h1=require("http");
h1.createServer((req,res)=>{ 
    res.write("welcome to http server class")
    res.end();

}).listen(8000)

var h1=require("http");
var p1=process.env.port||3000;
var server=h1.createServer((req,res)=>{
    res.write("<h1>hello</h1>");
    res.write("<h2>hello</h2>");
    res.write("<h3>hello</h3>");
    res.write("<h4>hello</h4>");
    res.write("<h5>hello</h5>");
    res.write("<h6>hello</h6>");
    res.end();




})

