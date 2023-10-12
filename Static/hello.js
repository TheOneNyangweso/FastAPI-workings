// Function myFunction() detects the value of current time and assigns appropriate value to msg var

function myFunction() {
    var today = new Date();
    var h = today.getHours();
    var m = today.getMinutes();
    var s = today.getSeconds();
    var msg = "";

    if (h < 12) {
        msg = "Good Morning, ";

    }
    if (h >= 12 && h < 18) {
        msg = "Good Afternoon, ";
        
    }
    if (h > 18) {
        msg = "Good Evening, ";

    }
    var x = document.getElementById('ttl').innerHTML;
    document.getElementById('ttl').innerHTML = msg + x;
    document.getElementById('time').innerHTML = h + ":" + m + ":" + s;
}