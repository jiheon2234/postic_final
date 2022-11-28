// 채용공고 키워드
const { children: titles } = document.querySelector(".animate-text");
const txtsLen = titles.length;
let index = 0;
const textInTimer = 3000;
const textOutTimer = 2800;

function animateText() {
  for (let i = 0; i < txtsLen; i++) {
    titles[i].classList.remove("text-in", "text-out");
  }
  titles[index].classList.add("text-in");

  setTimeout(function () {
    titles[index].classList.add("text-out");
  }, textOutTimer);

  setTimeout(function () {
    if (index == txtsLen - 1) {
      index = 0;
    } else {
      index++;
    }
    animateText();
  }, textInTimer);
}

window.onload = animateText;

// 총 채용건수
let number = document.getElementById("number");

let start = 20;
let end = 61782;
let ticks = 40;
let speed = 50;

let randomNumbers = [end];

for (let i = 0; i < ticks - 1; i++) {
  randomNumbers.unshift(Math.floor(Math.random() * (end - start + 1) + start));
}

randomNumbers.sort((a, b) => {
  return a - b;
});

console.log(randomNumbers.length);

let x = 0;
let interval = setInterval(function () {
  number.innerHTML = randomNumbers.shift();

  if (++x === ticks) {
    window.clearInterval(interval);
  }
}, speed);
