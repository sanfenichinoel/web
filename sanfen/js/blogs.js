
function showMarkdown(name) 
{
    var file = "./md/" + name;
    // console.log(file);
    var xmlhttp = new XMLHttpRequest();

    xmlhttp.onreadystatechange = function () {
        if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {
            document.getElementById("file" + name).innerHTML = marked(xmlhttp.responseText);
        }
    }
    xmlhttp.open("GET", file, true);
    xmlhttp.send();
}

function getfiles()
{
    let files = [];
    let xhr = new XMLHttpRequest();

    xhr.open("get","http://sanfensum.cn:8010/api/", false);
    xhr.send();
    files = xhr.responseText;
    files = JSON.parse(files);
    console.log(files);

    for(let i = 0;i < files.length;i++){
        let file = files[i];

        document.write(" \
            <div class=\"blogs_list\" id=\"file" + file + "\"> \
            \
            </div> \
            <script>showMarkdown(\"" + file + "\"); \
                console.log(\"" + file + "\"); \
            </script>"
        );
    }
}

