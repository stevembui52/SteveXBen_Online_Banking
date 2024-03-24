const hamburger=document.querySelector(".hamburger");
 const Navmenu=document.querySelector(".nav-list");

hamburger.addEventListener("click", ()=>{
    hamburger.classList.toggle("active");
   Navmenu.classList.toggle("active");
})