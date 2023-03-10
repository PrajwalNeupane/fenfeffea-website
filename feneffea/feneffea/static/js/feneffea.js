const hamburger = document.querySelector(".hamburger");
const navMenu = document.querySelectorAll(".nav-menu");
const bottom = document.querySelector(".bottom")

hamburger.addEventListener("click", () => {
  hamburger.classList.toggle("active");
  navMenu.classList.toggle("active");
  bottom.classList.toggle("active");
})

document.querySelectorAll(".nav-link").forEach(n => n.addEventListener("click", () => {
  hamburger.classList.remove("active");
  navMenu.classList.remove("active");
  bottom.classList.remove("active");
}))

console.log('hl')

navMenu.addEventListener("click", ()=>{
  navMenu.classList.toggle("active-nav")
})