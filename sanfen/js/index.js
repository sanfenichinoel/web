function sayxun()
{
    let str = "好菜 好菜 好菜 好菜 好菜";
    let output = document.getElementById("myxun");
    let i = 0;
    let timer = setInterval( 
        function () {
            output.innerHTML = str.substring(0, i);
            i++;
            if(output.innerHTML == str){
                // clearInterval(timer);
                i = 0;
            }
        },
        120
    )
}

function rand()
{
    let min_num = document.getElementById("minn").value
    console.log(min_num);
    let txt = document.getElementById("rand");
    txt.innerHTML = "";
    let x = Math.ceil( Math.random() * 100 );

    for(let i = 0;i < min_num;i++){
        txt.innerHTML += x;
        txt.innerHTML += " ";
        x = Math.ceil( Math.random() * 100 );

    }
}
