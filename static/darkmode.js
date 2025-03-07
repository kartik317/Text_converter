let darkmode = localStorage.getItem('darkmode');

const themeSwitch = document.getElementById('theme-switch');

const enableDarkmode = () => {
  document.body.classList.add('darkmode');
  localStorage.setItem('darkmode', 'active');
};

const disableDarkmode = () => {
  document.body.classList.remove('darkmode');
  localStorage.setItem('darkmode', null);
};

if (darkmode === "active") {
  enableDarkmode();
}

themeSwitch.addEventListener("click", () => {
  darkmode = localStorage.getItem('darkmode');
  darkmode !== "active" ? enableDarkmode() : disableDarkmode();
});


setTimeout(() => {
    const alerts = document.querySelectorAll('.alert');
    alerts.forEach(function(alert) {
        alert.style.transition = 'opacity 0.5s';
        alert.style.opacity = '0';
            
setTimeout(() => {
			alert.remove();
        }, 500);
    });
}, 2000);