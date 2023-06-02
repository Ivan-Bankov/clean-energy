function displayNav() {
    if(document.getElementById("mobile-nav-btn").checked) {
        document.getElementById("mobile-nav").style.transform = "translateX(-100%)";
        
    } else{
        document.getElementById("mobile-nav").style.transform = "translateX(100%)";
    }
}