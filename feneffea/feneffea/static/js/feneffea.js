// const hamburger1 = document.querySelector(".hamburger");
// const navMenu = document.querySelectorAll(".nav-menu");
// const bottom = document.querySelector(".bottom")
// const dropDownHeaders = document.querySelectorAll('.dropdown-header')
// const dropDownMenus = document.querySelectorAll('.dropdown-menu')

// hamburger1.addEventListener("click", () => {
//   hamburger1.classList.toggle("active");
//   for (const nav1 of navMenu){
//     nav1.addEventListener("click", () => {
//       nav1.classList.toggle("active")
//     });
//   };
//   bottom.classList.toggle("active");
// })

// document.querySelectorAll(".nav-link").forEach(n => n.addEventListener("click", () => {
//   hamburger1.classList.remove("active");
//   for (const nav2 of navMenu){
//     nav2.addEventListener("click", () => {
//       nav2.classList.remove("active")
//     })
//   }
//   bottom.classList.remove("active");
// }))

// dropDownHeaders.forEach((dropDownHeader) => {
//   dropDownHeader.addEventListener("click", () => {
//     if (dropDownHeader.children[1].classList.contains('active')){
//       dropDownHeader.children[1].classList.remove('active');
//     } else {
//       dropDownHeader.children[1].classList.add('active')
//     }
//   })
// })

document.addEventListener('DOMContentLoaded', () => {
  const hamburger = document.querySelector('.hamburger');
  const navLinks = document.querySelector('.nav-links');
  const dropdowns = document.querySelectorAll('.dropdown');

  hamburger.addEventListener('click', () => {
    navLinks.classList.toggle('active');
  });

  dropdowns.forEach((dropdown) => {
    dropdown.addEventListener('click', (event) => {
      if (window.innerWidth < 768) {
        event.preventDefault();
        const dropdownMenu = dropdown.querySelector('.dropdown-menu');
        dropdownMenu.classList.toggle('active');
      }
    });
  });
});

document.getElementById("contact-form").addEventListener("submit", function(event) {
  event.preventDefault();

  const email = document.getElementById("email").value;
  const name = document.getElementById("name").value;
  const subject = document.getElementById("subject").value;
  const message = document.getElementById("message").value;

  if (!validateEmail(email)) {
    alert("Please enter a valid email address.");
    return;
  }

  if (name.trim() === "" || subject.trim() === "" || message.trim() === "") {
    alert("Please fill in all the fields.");
    return;
  }

  alert("Your message has been sent successfully!");
  event.target.reset();
});

function validateEmail(email) {
  const regex = /^[\w-]+(\.[\w-]+)*@([\w-]+\.)+[a-zA-Z]{2,7}$/;
  return regex.test(email);
}



