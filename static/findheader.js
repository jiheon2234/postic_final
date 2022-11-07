const sidebar = document.getElementById("sidebar");
const stat_ul = document.getElementById("stat");
const keyword_ul = document.getElementById("keyword");
const pwd = window.location.pathname;

function findheader() {
  if (pwd.includes("stat")) {
    stat_ul.classList.add("show");
  } else if (pwd.includes("keyword")) {
    keyword_ul.classList.add("show");
  } else {
    return 0;
  }
  const active = document.getElementById(pwd);
  // console.log(active);
  active.classList.add("active");
}
document.addEventListener("DOMContentLoaded", findheader);
