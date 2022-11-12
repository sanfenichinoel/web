
function GetFile()
{
    let path = "../md/";

    let files = [];
    var fs = require('fs');
    let _files = fs.readdirSync(path);
    
    _files.forEach(function (item) {
        files.push(item);
    })
    let myfile = JSON.stringify(files);
    return myfile;
}


express = require("express")
cors = require("cors")

let app = express();
app.use(cors());
app.get("/api", function(rep, que){
    que.send(GetFile())
    // que.send("hello");
})

app.listen(8010);
