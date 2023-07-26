const hamburger = document.querySelector('.hamburger');
const navLinks = document.querySelector('.nav-links');
const dropdowns = document.querySelectorAll('.dropdown');


hamburger.addEventListener('click', () => {
  navLinks.classList.toggle('active');
});

// Event listener for dropdown menus
dropdowns.forEach((dropdown) => {
  const subDropdownMenu = dropdown.querySelector('.dropdown-menu');
  let isOpen = false;

  // Function to close the sub-dropdown menu
  const closeSubDropdownMenu = () => {
    subDropdownMenu.classList.remove('active');
    isOpen = false;
  };

  // Toggle the active class for sub-dropdown menus when a dropdown is clicked
  dropdown.addEventListener('click', (event) => {
    if (isOpen) {
      closeSubDropdownMenu();
    } else {
      closeAllSubDropdowns();
      subDropdownMenu.classList.add('active');
      isOpen = true;
    }
    event.stopPropagation();
  });
});










