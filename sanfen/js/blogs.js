
function showMarkdown(name) 
{
    document.getElementById("filetitle" + name).innerHTML = name;

    var file = "./md/" + name + ".md";
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
        // let fileurl = encodeURI(file);
        document.write
        ("                                                                                              \                                                                                         \
            <div class=\"blogs_list\" >                                                                 \
                <a class=\"file_title\" id=\"filetitle" + file + "\" href=\"blog.html?name=" + file + "\" target=\"_blank\" rel=\"noopener noreferrer\">                         \
                        标题                                                                                \
                </a>                                                                                       \
                <div class=\"file_other\" id=\"file" + file + "\">                                 \
                        主体预览                                                                         \
                </div>                                                                                  \
            </div>                                                                                      \
            <script>                                                                                \
                showMarkdown(\"" + file + "\");                                                     \
            </script>                                                                               \                                                                                     \
        ");
    }
}

