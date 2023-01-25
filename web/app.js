const title = document.querySelector(".title");
const btnList = document.querySelector(".genlist");
const btnDic = document.querySelector(".gendic");
const btnPrint = document.querySelector(".genprint")
const txt = document.querySelector(".typetxt");

btnList.addEventListener("click", () => {
    tmp = "";

    if (document.querySelector(".listchar").value === "/n") {
        tmp = txt.value.split("\n");
    } else {
        tmp = txt.value.split(document.querySelector(".listchar").value);
    }


    for (i = 0; i < tmp.length; i++) {
        tmp[i] = "\"" + tmp[i] + "\" ";
    }
    console.log("[" + tmp.toString() + "]")

    navigator.clipboard.writeText("[" + tmp.toString() + "]").then(function() {
        title.textContent = "Code Generated!";
    })
})

btnDic.addEventListener("click", () => {
    let result = {}
    let tmp = "";

    if (document.querySelector(".dicchar").value === "/n") {
        tmp = txt.value.split("\n");
    } else {
        tmp = txt.value.split(document.querySelector(".dicchar").value);
    }

    for (i = 0; i < tmp.length; i++) {
        result[tmp[i].split(document.querySelector(".keychar").value)[0]] = tmp[i].split(document.querySelector(".keychar").value)[1];
    }

    console.log(JSON.stringify(result));
    navigator.clipboard.writeText(JSON.stringify(result)).then(function() {
        title.textContent = "Code Generated!";
    })
})


btnPrint.addEventListener("click", () => {
    let tmp = "";
    let result = "";

    if (document.querySelector(".listchar").value === "/n") {
        tmp = txt.value.split("\n");
    } else {
        tmp = txt.value.split(document.querySelector(".listchar").value);
    }

    for (i = 0; i < tmp.length; i++) {
        result += document.querySelector(".printchar").value + "(\"" + tmp[i] + "\")\n";
    }

    navigator.clipboard.writeText(result).then(function() {
        title.textContent = "Code Generated!";
    })
})