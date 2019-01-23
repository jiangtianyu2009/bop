var quan_time = "20181216175500";
setInterval(function () { getTime() }, 1000);
function getTime() {
    $.ajax({
        type: "get", url: "https://quan.suning.com/getSysTime.do", async: true, success: function (data) {
            var data = eval("(" + data + ")");
            console.log(data.sysTime1);
            if (data.sysTime1 == quan_time) { setTimer() }
        }
    })
}
function setTimer() {
    var i = 1;
    var timer = setInterval(function () {
        if (i > 4) { clearInterval(timer) }
        else {
            receiveCoupon("201812100004014026", "X3x1HWXxtjfcyeI8ylOsj4O7", "3", "10004");
            console.log(i);
            i++
        }
    }, 300)
};