let my_profile = document.querySelector(".my_profile")
let disp = false
my_profile.style.display = 'none'
function profile_click(){
if (disp) {
    my_profile.style.display = 'none'
    disp = false
}else{
    my_profile.style.display = 'block'
    disp = true
}

}